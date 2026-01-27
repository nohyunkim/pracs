# 역할: 사용자가 입력한 기상 시간에 맞춰, 90분 수면 주기를 기반으로 최적의 취침 시간을 추천합니다.
# 사용 모듈: datetime (시간 및 날짜 계산)

import datetime

def calculate_optimal_sleep_times():
    """ 기상 시간을 입력받아, 4~6회의 수면 주기를 역산하여 가장 개운하게 일어날 수 있는 취침 시간을 추천하는 함수"""
    
    # 2. 프로그램이 시작되면 내일 일어나야 될 시간 (예 : 07:00)을 입력
    wake_up_input = input("🌞 내일 일어나고 싶은 시간을 'HH:MM' 형식으로 입력하세요 (예: 08:30): ")

    try:
        # 입력받은 시간을 파싱하여 datetime 객체로 변환
        wake_up_time = datetime.datetime.strptime(wake_up_input, "%H:%M")

        print(f"\n내일 아침 {wake_up_time.strftime('%H:%M')}에 상쾌하게 일어나려면,")
        print("아래 시간들에 잠드는 것이 좋습니다.\n")

        # 3. 입력된 시간으로부터 90분 간격으로 역산해서 최적의 취침 시간을 추천
        # 일반적으로 5~6 사이클(7.5~9시간) 수면이 가장 이상적입니다.
        for i in range(6, 3, -1):
            # 수면 주기 (90분) * 사이클 횟수
            total_sleep_minutes = 90 * i
            
            # 기상 시간에서 총 수면 시간을 빼서 취침 시간 계산
            sleep_time = wake_up_time - datetime.timedelta(minutes=total_sleep_minutes)
            
            # 총 수면 시간을 'O시간 O분' 형식으로 변환
            hours, minutes = divmod(total_sleep_minutes, 60)
            sleep_duration_str = f"{hours}시간"
            if minutes > 0:
                sleep_duration_str += f" {minutes}분"

            # 4. 출력할 때 추천 : 밤 11시 이런식으로 보기좋게 출력
            # 밤/오후/오전 구분
            if sleep_time.hour >= 21 or sleep_time.hour < 5:
                period = "밤"
            elif sleep_time.hour >= 12:
                period = "오후"
            else:
                period = "오전"

            # 12시간제 형식으로 변환 (예: 23:30 -> 밤 11:30)
            formatted_sleep_time = sleep_time.strftime("%I:%M")

            print(f"추천 {7-i}: {period} {formatted_sleep_time} ({sleep_duration_str} 수면)")

    except ValueError:
        print("\n❌ 잘못된 형식입니다. 'HH:MM' 형식에 맞춰 다시 입력해주세요.")

# 이 스크립트 파일이 직접 실행될 때만 함수를 호출
if __name__ == "__main__":
    calculate_optimal_sleep_times()
