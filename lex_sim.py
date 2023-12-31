'''
s: "ab12c"
t: "1zz456"
1

s: "d"
t: "6"
0

For s = "ab12c" and t = "ab24z", the output should be solution(s, t) = 3.
'''

def find_variants(w):
    w_variants = []
    for i in range(len(w)):
        if w[i].isdigit() == True:
            variant = w[:i] + w[i+1:]
            #print(i, variant)
            w_variants.append(variant)
    return w_variants
    
def is_w1_lexsmall_than_w2(w1, w2):
    i = 0
    w1_is_lex_small = False
    while True:
        w1_len, w2_len = len(w1), len(w2)
        w1_c, w2_c = "", ""
        
        if w1_len <= i: w1_is_lex_small = True; break
        if w2_len <= i: w1_is_lex_small = False; break
        
        w1_c, w2_c = w1[i], w2[i]
        if w1[i] == w2[i]: 
            i += 1
            continue
            
        if w1[i] < w2[i]:   w1_is_lex_small = True; break
        if w1[i] > w2[i]:   w1_is_lex_small = False; break
    #print(w1_is_lex_small, w1_c, w2_c)
    return w1_is_lex_small


def solution(s, t):
    #print("s", s)
    #print("t", t)
    # identify the integers in each string and store the rest of the string
    s_variants = find_variants(s)
    t_variants = find_variants(t)
    
    count = 0
    for s_variant in s_variants: 
        if is_w1_lexsmall_than_w2(s_variant, t) == True:
            count += 1
    #print(count)
            
    for t_variant in t_variants: 
        if is_w1_lexsmall_than_w2(s, t_variant) == True:
            count += 1
    
    #print(count)
    return count

