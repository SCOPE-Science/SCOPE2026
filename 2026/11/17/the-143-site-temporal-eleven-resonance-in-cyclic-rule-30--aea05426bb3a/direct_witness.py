"""Direct ring-only check independent of the temporal-column recurrence."""
from pathlib import Path
p=Path(__file__).resolve().parent
records={}
for row in (p/'cycle_walk_output.txt').read_text().splitlines():
    if row.startswith('witness_'):
        key,bits=row.split('=',1)
        records[int(key.split('_')[1])]=bits

def f(s):
    return ''.join(str((int(s[i-1]) ^ (int(s[i]) | int(s[(i+1)%len(s)])))) for i in range(len(s)))
for length,word in sorted(records.items()):
    assert len(word)==length
    assert len(set(word))==2
    x=word
    for t in range(1,12):
        x=f(x)
        assert (x==word)==(t==11), (length,t)
    assert all(any(word[i]!=word[i%d] for i in range(length)) for d in range(1,length) if length%d==0)
    print('length',length,'primitive_temporal_period=11','primitive_spatial_period='+str(length), 'ones='+str(word.count('1')))
