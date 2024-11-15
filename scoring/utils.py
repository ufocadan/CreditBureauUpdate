from .models import UserResponse, Question

def calculate_credit_score(user_id):
    user_responses = UserResponse.objects.filter(user_id=user_id)
    total_score = 0

    for response in user_responses:
        question = response.question
        if response.answer == 'A':
            total_score += question.score_a
        elif response.answer == 'B':
            total_score += question.score_b
        elif response.answer == 'C':
            total_score += question.score_c
        elif response.answer == 'D':
            total_score += question.score_d

    return total_score