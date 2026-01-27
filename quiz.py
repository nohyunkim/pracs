# quiz.py

def run_quiz():
    # 1. 파이썬의 딕셔너리(dictionary) 기능을 사용해서 '데이터' 관련 용어 5개와 정답을 미리 저장
    quiz_data = {
        "정형 데이터": "데이터베이스",
        "비정형 데이터": "텍스트, 이미지, 음성",
        "반정형 데이터": "JSON, XML, HTML",
        "빅데이터": "대규모 데이터",
        "데이터 마이닝": "데이터에서 유용한 패턴 발견"
    }

    score = 0
    total_questions = len(quiz_data)

    print("ADSP 데이터 관련 용어 퀴즈를 시작합니다!")
    print("-----------------------------------")

    # 2. 프로그램을 실행하면 문제(뜻)가 나오고, 내가 답을 입력하면 정답인지 오답인지 알려주는 기능
    for question, correct_answer in quiz_data.items():
        print(f"\n문제: {question}에 대한 예시는 무엇일까요?")
        user_answer = input("당신의 답변: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 '{correct_answer}'입니다.")
    
    print("\n-----------------------------------")
    # 3. 마지막에 몇 개 맞췄는지 점수도 알려줘.
    print(f"퀴즈가 종료되었습니다. {total_questions}문제 중 {score}문제를 맞추셨습니다!")
    print(f"당신의 점수는 {score}/{total_questions} 입니다.")

if __name__ == "__main__":
    run_quiz()
