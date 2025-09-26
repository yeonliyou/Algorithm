# 5653.줄기세포 배양
# 줄기세포들을 배양 용기에 도포하고, 
# 일정 시간 동안 배양 시키고 나서 줄기 세포 개수가 몇개가 되는지 계산
# 생명력 수치가 X인 줄기 세포는 X시간 동안 비활성화, X시간 지나는 순간 활성화
# 활성화 된 시점부터 X시간 동안 후에 죽게됨
# 죽는다고 소멸되는건 아니고 죽은 상태로 셀에 남아있음
# 활성화된 줄기세포는 "첫 1시간" 동안 상하좌우 네방향을 동시번식
# 번식된 줄기 세포는 비호라성 상태
# 번식하고 싶은 방향에 이미 줄기세포가 존재하면 추가적으로 번식하진 않음
# 두 개 이상의 줄기 세포가 하나의 그리드 셀에 동시 번식하려고 하면 생명력 높은 세포가 혼자 차지
# 답 : K시간 후 살아 있는 줄기 세포(비활성 + 활성 상태) 총 개수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    # 초기 상태일때 줄기 세포 분포된 영역의 세로, 가로 / 배양시간 K
    N, M, K = map(int, input().split())
    init_grid = [list(map(int, input().split())) for _ in range(N)]

    # 격자 크기 확장 (무한대 대신 N+2K, M+2K로 충분)
    SIZE = N + 2*K
    OFFSET = K  # 원래 좌표를 중앙으로 밀기 위한 offset

    grid = [[0]*SIZE for _ in range(SIZE)]
    # 살았는지 죽었는지 여부
    live = [[0]*SIZE for _ in range(SIZE)]  # 0 빈칸, 1 비활성, 2 활성, -1 죽음
    X_time = [[0]*SIZE for _ in range(SIZE)]  # 남은 시간 관리

    # 1. 격자 늘려서 붙이기 - 0초 셀들 셋팅 시작
    # 행
    for r in range(N):
        # 열
        for c in range(M):
            if init_grid[r][c] > 0:
                # 중앙으로 밀어주기 (해당 셀 기준으로 K만큼 뒤로 밀어준것)
                n_r = r + OFFSET
                n_c = c + OFFSET
                # 새로운 무한 격자에 값 갱신
                grid[n_r][n_c] = init_grid[r][c]
                live[n_r][n_c] = 1  # 첫 체크
                X_time[n_r][n_c] = grid[n_r][n_c]  # 초기 X시간 기록용

    # 2. t초 동안 돌기
    for t in range(1, K+1):
        # 이번 턴에서 새로 번식할 후보 저장 (동시에 같은 칸에 번식하려는 경우를 처리하려고 사용)
        new_cells = set()
        
        # 행 열 돌기
        for r in range(SIZE):
            for c in range(SIZE):
                # 비활성화라면
                if live[r][c] == 1:
                    # 시간 차감해주기
                    X_time[r][c] -= 1
                    # 만약 활성 시작할 수 있는 상태가 되면
                    if X_time[r][c] == 0:
                        live[r][c] = 2  # 활성으로 전환
                        X_time[r][c] = grid[r][c]  # 활성 시간 다시 세팅

                # 활성 상태라면
                elif live[r][c] == 2:
                    # 시간 차감
                    X_time[r][c] -= 1

                    # 활성 첫 1시간 이라면 번식함
                    if X_time[r][c] == grid[r][c]-1:  
                        for idx in range(4):
                            n_r = r + dx[idx]
                            n_c = c + dy[idx]

                            # 만약 번식하려는 칸이 비어있으면
                            if live[n_r][n_c] == 0:
                                # 번식된 X 종류, 갱신 행, 갱신 열
                                new_cells.add((grid[r][c], n_r, n_c))
                    
                    # 활성상태였는데 이제 남은 시간이 없으면 죽음으로 처리
                    if X_time[r][c] == 0:
                        live[r][c] = -1

        # 새로 번식한 세포 반영
        for X, r, c in new_cells:
            # 빈칸이면
            if grid[r][c] == 0:
                grid[r][c] = X
            else:
                # 기존값 vs 현재 들어온 값 비교
                grid[r][c] = max(grid[r][c], X)
                
            live[r][c] = 1
            X_time[r][c] = grid[r][c]

    # 살아있는 세포 개수 세기
    anw = 0
    for r in range(SIZE):
        for c in range(SIZE):
            # 살아있으면 카운트 +1
            if live[r][c] >= 1:
                anw += 1

    print(f"#{tc}", anw)
