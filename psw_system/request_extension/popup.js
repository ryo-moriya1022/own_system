chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "sendDataToPopup") {
    // メッセージが受信されたときの処理
    console.log("Data received in popup.js:", request.data);
  }
});
