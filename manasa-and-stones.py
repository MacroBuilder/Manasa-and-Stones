def manasa(N,A,B):
    possible = []
    for x in range(N):
        steps = max(A,B)*x + min(A,B)*(N-1-x)
        if steps not in possible:
            possible.append(steps)
    print ' '.join(map(str,possible))

test_cases = int(raw_input().strip())

for _ in range(test_cases):
    n,a,b = int(raw_input().strip()), int(raw_input().strip()), int(raw_input().strip())
    manasa(n,a,b)
