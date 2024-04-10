document.getElementById("questionForm").addEventListener("submit",
function(event){
    event.preventDefault();//need to not refresh page

    var question=document.getElementById("question").value;

    chrome.runtime.sendMessage({ action: "sendDataToServer", data:question});

}
)
