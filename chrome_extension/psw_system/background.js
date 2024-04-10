chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if (request.action === "sendDataToServer") {
      input()
        .then(data => {
          chrome.runtime.sendMessage({ action: "sendDataToPopup", data: data });
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
    }
  }
);

async function input() {
  var url = "http://127.0.0.1:8000";
  try {
    const response = await fetch(url);

    console.log("fetchが実行されました");
    console.log("Response Status: " + response.status);

    // レスポンスのJSONデータを取得
    const data = await response.json();
    console.log(data);

    // popup.jsにデータとステータスコードを返す
    return { data: data, status: response.status };
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
    throw error;
  }
}
