#!/usr/bin/env python3
"""Independent exact Moore refinement of all binary four-factor exemption languages."""
from collections import deque

EXPECTED=(8435,11121,9670,10152,9956,9537,8524,11746,
          11746,8524,9537,9956,10152,9670,11121,8435)

def build(k=4):
    states=[(0,'')]
    lookup={states[0]:0}
    transitions=[]
    for mask,suffix in states:
        out=[]
        for bit in '01':
            new=suffix+bit
            newmask=mask | ((1<<int(new,2)) if len(new)==k else 0)
            nxt=(newmask,new[-(k-1):])
            if nxt not in lookup:
                lookup[nxt]=len(states)
                states.append(nxt)
            out.append(lookup[nxt])
        transitions.append(tuple(out))
    return states,transitions

def refine(states,edges,excluded):
    target=((1<<16)-1) ^ (1<<excluded)
    accept=[(m&target)==target for m,s in states]
    colors=[int(v) for v in accept]
    levels=[len(set(colors))]
    while True:
        signatures=[(colors[i],colors[edges[i][0]],colors[edges[i][1]])
                    for i in range(len(edges))]
        dictionary={}
        updated=[]
        for signature in signatures:
            if signature not in dictionary: dictionary[signature]=len(dictionary)
            updated.append(dictionary[signature])
        levels.append(len(dictionary))
        if len(dictionary)==levels[-2]:
            colors=updated
            break
        colors=updated
    representatives={}
    for i,c in enumerate(colors):
        signature=(accept[i],colors[edges[i][0]],colors[edges[i][1]])
        if c in representatives: assert representatives[c]==signature
        else: representatives[c]=signature
    assert len(representatives)==levels[-1]
    return len(representatives),len(levels)-2,levels

def brute_accept(word,excluded):
    required={format(i,'04b') for i in range(16) if i!=excluded}
    return required.issubset({word[i:i+4] for i in range(len(word)-3)})

def main():
    states,edges=build()
    assert len(states)==19205,len(states)
    for excluded,expect in enumerate(EXPECTED):
        count,depth,levels=refine(states,edges,excluded)
        assert count==expect,(excluded,count,expect)
        assert depth==(17 if excluded in (0,15) else 18),(excluded,depth)
        assert levels[-1]==levels[-2] and levels[-3]<levels[-2]
        for length in range(0,11):
            for val in range(1<<length):
                word=format(val,'0%db'%length) if length else ''
                state=0
                for b in word: state=edges[state][int(b)]
                assert ((states[state][0]&(((1<<16)-1)^(1<<excluded)))==(((1<<16)-1)^(1<<excluded)))==brute_accept(word,excluded)
        print(f'{excluded:04b}: reachable={len(states)} minimal={count} max_distinguishing_suffix_length={depth}')
    # Check positive accepted witnesses as well as rejecting short inputs.
    for pattern in range(16):
        found=False
        for bits in range(1<<18):
            word=f'{bits:018b}'
            seen={word[j:j+4] for j in range(15)}
            if len(seen)==15 and format(pattern,'04b') not in seen:
                state=0
                for bit in word:state=edges[state][int(bit)]
                mask=states[state][0]
                target=65535 ^ (1<<pattern)
                assert (mask&target)==target and brute_accept(word,pattern)
                found=True
                break
        assert found,pattern
    print('Positive witnesses of length 18: ALL 16 PASS')
    print('Moore refinement: ALL 16 EXACT COUNTS PASS')
if __name__=='__main__':main()
