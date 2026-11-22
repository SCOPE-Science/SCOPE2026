"""Independent literal-string replay for the listed universal binary four-mer greedy merge histories."""
from pathlib import Path
import sys

def overlap(a,b):
    return max([k for k in range(1,min(len(a),len(b))+1) if a[-k:]==b[:k]]+[0])

def verify(path):
    lines=Path(path).read_text(encoding='utf-8').splitlines()
    assert lines[0].startswith('states=2262207 lengths=')
    assert set(map(int,lines[0].split('lengths=')[1].strip(',').split(',')))==set(range(19,28))
    for line in lines[1:]:
        pre,steps=line.split(' merges=')
        target=int(pre.split(' ')[0][2:]);result=pre.split(' result=')[1]
        words={i:format(i,'04b') for i in range(16)}
        trails={i:[i] for i in range(16)}
        for step in steps.rstrip(';').split(';'):
            fi,li,fj,lj,saved=map(int,step.split(','))
            assert fi!=fj and fi in words and fj in words
            assert trails[fi][-1]==li and trails[fj][-1]==lj
            m=max(overlap(x,y) for i,x in words.items() for j,y in words.items() if i!=j)
            assert saved==m==overlap(words[fi],words[fj])
            words[fi]=words[fi]+words[fj][saved:]
            trails[fi].extend(trails[fj])
            del words[fj],trails[fj]
        assert len(words)==1 and len(trails[next(iter(trails))])==16
        assert result==next(iter(words.values())) and len(result)==target
        assert {result[i:i+4] for i in range(len(result)-3)}=={format(i,'04b') for i in range(16)}
        print(f'PASS length={target} steps=15 full-spectrum=16')
    assert len(lines)==10
if __name__=='__main__':
    verify(sys.argv[1] if len(sys.argv)>1 else 'witnesses.txt')
