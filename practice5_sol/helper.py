import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def wait_for_element(driver, by_locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located(by_locator))

def wait_for_alert(driver, timeout=5):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.alert_is_present())

def read_csv(file_path):
    """
    CSV 파일을 읽어 유효한 row만 딕셔너리 리스트로 반환
    - csv.DictReader 사용
    - (추가문제) 유효하지 않은 row는 제외하고 콘솔에 로깅
    """
    data_list = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for line_no, row in enumerate(reader, start=2):  # 헤더 다음 줄부터
            text = row.get("text", "").strip()
            email = row.get("email", "").strip()
            pwd = row.get("pwd", "").strip()

            ## 추가문제: 데이터 유효성 검사
            EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
            
            if not text:
                print(f"[SKIP][Line {line_no}] text 비어있음 → {row}")
            elif not email:
                print(f"[SKIP][Line {line_no}] email 비어있음 → {row}")
            elif not EMAIL_REGEX.match(email):
            # elif '@' in text: # 단순히 @ 포함 여부만 검사
                print(f"[SKIP][Line {line_no}] email 형식 오류 → {row}")
            else:
                # 유효한 데이터만 추가
                data_list.append({
                    "text": text,
                    "email": email,
                    "pwd": pwd
                })

    return data_list

