# quiz.py

# 기능: ADSP 데이터 용어 퀴즈를 실행하고 결과를 채점합니다.
# 특징:
# 1. random 모듈을 사용하여 문제 순서가 매번 무작위로 출제됩니다.
# 2. enumerate를 활용하여 현재 풀고 있는 문제 번호를 (예: "문제 [1/5]") 표시합니다.
# 3. 정답/오답 여부를 이모지(✅, ❌)로 명확하게 보여줍니다.

import random # 1. 무작위 순서 섞기를 위한 random 모듈 불러오기

def run_quiz():
    # 퀴즈 데이터 정의 (Key: 문제, Value: 정답)
    quiz_data = {
        "정형 데이터": "데이터베이스",
        "비정형 데이터": "텍스트, 이미지, 음성",
        "반정형 데이터": "JSON, XML, HTML",
        "빅데이터": "대규모 데이터",
        "데이터 마이닝": "데이터에서 유용한 패턴 발견"
    }

    # 점수 및 전체 문항 수 변수 초기화
    score = 0
    total_questions = len(quiz_data)

    print("✨ ADSP 데이터 용어 퀴즈 ✨")

    # 문제 순서 섞기
    # quiz_data.items()로 (문제, 정답) 쌍을 가져와 리스트로 만들고, 순서를 섞습니다.
    quiz_items = list(quiz_data.items())
    random.shuffle(quiz_items)

    # 섞인 문제 리스트를 순회하며 퀴즈 진행
    # enumerate를 사용해 1부터 시작하는 문제 번호(idx)를 함께 가져옵니다.
    for idx, (question, correct_answer) in enumerate(quiz_items, 1):
        # 2. 현재 문제 진행 상황 출력
        print(f"\n문제 [{idx}/{total_questions}]: '{question}'의 대표적인 예시는 무엇일까요?")
        user_answer = input("답변: ").strip()

        # 정답 비교 (사용자 입력과 정답을 모두 소문자로 변경하여 비교)
        if user_answer.lower() == correct_answer.lower():
            # 3. 정답 시 피드백
            print("✅ 정답!")
            score += 1
        else:
            # 3. 오답 시 피드백
            print(f"❌ 땡! 정답은 '{correct_answer}'입니다.")
    
    # 최종 결과 출력
    print("🎉 퀴즈가 종료되었습니다! 🎉")
    print(f"결과: {total_questions}문제 중 {score}문제를 맞혔습니다.")
    print(f"총점: {score}/{total_questions}")

# 이 스크립트 파일이 직접 실행될 때만 run_quiz() 함수를 호출
if __name__ == "__main__":
    run_quiz()
