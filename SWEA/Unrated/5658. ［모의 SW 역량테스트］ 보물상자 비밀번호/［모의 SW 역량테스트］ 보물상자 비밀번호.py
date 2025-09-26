# 5658. 보물상자 비밀번호

# N은 4의 배수
# 3회전 하면 처음 배치와 같아짐 (회전 주기 3 만큼 계속 배치가 같아짐)

T = int(input())

# 십진수 만드는 함수
def make_ten(target : list):
    target = ''.join(target)
    num = int(target, 16)
    return num

for tc in range(1, T+1):
    # 숫자의 개수, 크기 순서
    N, K = map(int, input().split())

    # 16진수 rotation 돌 스택
    stack = list(input().strip())

    # 10진수를 저장할 리스트
    ten_nums = []

    # N번 회전하기
    for _ in range(N):
        # 첫 인덱스
        start_idx = 0
        # 4개의 변 돌기
        for _ in range(4):
            # 10진수로 변환 (N//4 만큼 끊기)
            num = make_ten(stack[start_idx : start_idx + N//4])
            # 만약 중복된 수가 아니라면 리스트에 넣어주기
            if num not in ten_nums:
                ten_nums.append(num)

            # 시작 인덱스 뒤로 N//4 미루기
            start_idx += N//4

        # 맨 앞에 있는 숫자 빼기
        curr_first = stack.pop(0)
        # curr_first 맨뒤로 옮겨주기
        stack.append(curr_first)

    # 내림차순으로 정렬
    ten_nums = sorted(ten_nums, reverse = True)

    anw = ten_nums[K-1]

    print(f"#{tc}", anw)