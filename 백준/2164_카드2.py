num = int(input())
cards = [x for x in range(1, num+1)]
idx = 0
while len(cards) - idx > 1: # 길이와 index가 1 차이남 = 마지막까지 도달
    idx += 1 # 함으로써 삭제 효과
    cards.append(cards[idx]) # 뒤에 해당 숫자 추가
    idx += 1 # 앞에있던 원래 숫자 삭제 효과
print(cards[-1])