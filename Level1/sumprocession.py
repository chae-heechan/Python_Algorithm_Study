def solution(arr1, arr2):
    return [[c + d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)] 