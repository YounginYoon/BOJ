def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    answer = participant[-1]
    return answer