'''
arr: [9, 8, 7, 6, 5] output : 4
arr: [-778277028, -509675834, -828663475, 190114564, -34919218, -34919218, 106447210, -887980502, -399561546, -319453881, -319453881, 564702467, -512179848, 634452898, -279371457, -279371457, -72310717, -770556513, -629539596, 112073567]
output: 34
'''

def is_seq_saw_tooth(seq, start, prev_diff):
    
    diff, prev_diff=0, prev_diff
    saw_tooth = True
    i = start
    for i in range(start, len(seq)-1):
        diff = seq[i] - seq[i+1]
        if i>0:
            if ((diff < 0) and (prev_diff < 0)) or\
                ((diff > 0) and (prev_diff > 0)):
                saw_tooth = False
                break
        if diff == 0:
            saw_tooth = False
        prev_diff = diff
    return saw_tooth, i+1,  prev_diff, i+1-start
            
def solution(arr):
    NUM_FUNC_CALLS = 0
    NUM_ITERATIONS = 0
    
    len_arr = len(arr)
    count = 0
    for i in range(len_arr):
        j = i+2
        start_index, prev_diff = 0, 0
        while j <= len_arr:
            sub_arr = arr[i : j]
            res, last_index, last_prev_diff, num_iters = is_seq_saw_tooth(sub_arr, start_index, prev_diff)
            NUM_FUNC_CALLS += 1
            NUM_ITERATIONS += num_iters
            #print(i, j, sub_arr, res, last_index, prev_diff)
            if res == True: 
                start_index = last_index
                prev_diff = last_prev_diff
                count += 1
            else: 
                break
            j += 1
    
    print(count)   
    print("NUM_FUNC_CALLS", NUM_FUNC_CALLS, "NUM_ITERATIONS",NUM_ITERATIONS)
    return count