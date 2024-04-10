chrome.runtime.onMessage.addListener(
  async function(request, sender, sendResponse) {
    if (request.action === "sendDataToServer") {
      try {
        const responseData = await fetchData(request.data);
        chrome.runtime.sendMessage({ action: "sendDataToPopup", data: responseData });
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }
  }
);

async function fetchData(data) {
  var apikey = "AIzaSyC_MgvIo7ulAkU7HtqMubb0EeAkFiBIFyA"
  var url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${apikey}`;
  try {
    console.log("input form", data);
    console.log("fetchが実行されました");

    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "contents": [{
          "parts":[{
          "text": `今から英文を提出します。正しい英語か確認してください。もし違う場合は理由と修正した文章を一緒に教えてください。${data}`,
          }]
      }]
      })
    });

    console.log("Response Status: " + response.status);

    // レスポンスのJSONデータを取得
    const responseData = await response.json();
    console.log(responseData);

    // データとステータスコードを返す
    return { data: responseData, status: response.status };
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
    throw error;
  }
}
