# 4013번_특이한 자석
from collections import deque
#import sys

# 각 자석이 회전할건지 안할건지 체크하는 함수
def find_rotate_magnetic(curr_list):
    global flag, visited, magnets

    # curr_list 비울때까지 돌기
    while curr_list:
        curr_num, curr_dir = curr_list.pop(0)

        # 체크한적 없는 자석이라면
        if visited[curr_num] != True:
            # 체크 확인 여부 해주기
            visited[curr_num] = True

            # 1번 자석
            if curr_num == 1:
                if magnets[1][2] != magnets[2][6]:
                    flag[curr_num + 1] = curr_dir * -1
                    if not visited[curr_num + 1]:
                        curr_list.append((curr_num + 1, flag[curr_num + 1]))

            # 2번, 3번 자석
            elif curr_num == 2 or curr_num == 3:
                # 왼쪽 이웃 확인
                if magnets[curr_num - 1][2] != magnets[curr_num][6]:
                    flag[curr_num - 1] = curr_dir * -1
                    if not visited[curr_num - 1]:
                        curr_list.append((curr_num - 1, flag[curr_num - 1]))
                # 오른쪽 이웃 확인
                if magnets[curr_num][2] != magnets[curr_num + 1][6]:
                    flag[curr_num + 1] = curr_dir * -1
                    if not visited[curr_num + 1]:
                        curr_list.append((curr_num + 1, flag[curr_num + 1]))

            # 4번 자석
            elif curr_num == 4:
                if magnets[3][2] != magnets[4][6]:
                    flag[curr_num - 1] = curr_dir * -1
                    if not visited[curr_num - 1]:
                        curr_list.append((curr_num - 1, flag[curr_num - 1]))


#sys.stdin = open("4013_input.txt")

T = int(input())

for tc in range(1, T+1):
    # 회전 횟수 K
    K = int(input())

    # 1번부터 4번까지 자석 que 만들기
    magnets = [deque(map(int, input().split())) for _ in range(4)]
    magnets.insert(0, 0)  # 1-index

    # 최종 점수 스코어 초기화
    anw = 0

    # 회전 정보 리스트
    rotate_info = []

    # 회전 정보 받기
    for _ in range(K):
        # [자석의 번호, 회전 방향] 추가
        rotate_info.append(list(map(int, input().split())))

    # 회전 하기
    for _ in range(K):
        num, dir = rotate_info.pop(0)

        # -1, 0, 1은 순서대로 반시계, 회전안함, 시계
        flag = [0, 0, 0, 0, 0]

        # 체크 여부 확인
        visited = [False, False, False, False, False]

        # 현재 회전하고자 하는 자석에 해당 방향 넣어주기
        flag[num] = dir
        # 체크할 자석들 저장
        curr_list = [(num, dir)]

        # 전파 회전 결정
        find_rotate_magnetic(curr_list)

        # 실제 회전 수행
        for idx, dir in enumerate(flag):
            # 회전해야 하는 자석이라면 회전
            if idx != 0 and dir != 0:
                magnets[idx].rotate(dir)

    # 최종 점수 계산
    if magnets[1][0] == 1:
        anw += 1
    if magnets[2][0] == 1:
        anw += 2
    if magnets[3][0] == 1:
        anw += 4
    if magnets[4][0] == 1:
        anw += 8

    print(f"#{tc}", anw)
