import requests
import time
username = "b2222380"
password = "EVA1022moriya"
login_url = "https://portal.mc.chitose.ac.jp/portal2/j_security_check"


# セッションのインスタンスを作成する。
def session_portal():
    session = requests.Session()
    response_1 = session.post(
            url=login_url,
            data={
                "j_username": username,
                "j_password": password,
            },
            timeout=1
    )
    print("response1",response_1.url)
    test=response_1.url.split("?")
    time.sleep(1)
    urlt=f"https://portal.mc.chitose.ac.jp/portal2/CoursesForUser?{test[1]}-1.ILinkListener-chooseCoursesPanel-myCourses-16-lectureViewLink"
    url=""
    response_2=session.post(urlt)
    print(response_2.url)
    urlt=f"{response_2.url}-1.ILinkListener-chooseCoursesPanel-myCourses-16-lectureViewLink"
    response_3=session.post(urlt,
                        data={
                            "id20_hf_0":"",
                            "password":"abc",
                            "saveButton":"1"
                        }    )
    print("出席リクエスト",response_3.url)
    # 長いので出力略
    # ログイン後に表示される機能メニューのHTMLが得られている。
session_portal()