input()

async function input() {
    var url = "http://127.0.0.1:8001";
    var url="https://portal.mc.chitose.ac.jp/portal2/yb6VGTNWX7AT6jlYsmchExx3_3GnNw-NSPhmPaW8A80viE0WH7kjmzvQ7afNicKhEtg6CGIhf9TPjU566k8ZQLNW11Z1LLrdZNgahrmcv_qD-MlZJPA_6N1dkmzps2W0y9TdSa2t-QRZOS7y_ieIRy8s1IsaeFHtFevhnSyzHhthbyxeDJO42TDwNWTfD0bm/yb67c"
    const formData = new FormData();
// FormData にデータを追加
    formData.append('password', 'e7Gr');
    formData.append('saveButton', '1');
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
  