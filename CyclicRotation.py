def solution(A, K):
    if not A: 
        return A
    K = K % len(A)        #no need to flip more than necessary
    i = 0 
    while i < K:
        temp = A[-1]
        for idx in range(len(A)):
            a = A[idx]
            A[idx] = temp
            temp = a
        i += 1
    return A
