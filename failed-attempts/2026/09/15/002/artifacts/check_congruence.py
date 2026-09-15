from cypari2 import Pari
pari = Pari()
pari('MF = mfinit([109,2,1])')
pari('E = mfeigenbasis(MF)')
for i in (1,2,3):
    pari('F%d = E[%d]' % (i,i))
# q-expansions to 200
for i in (1,2,3):
    pari('c%d = mfcoefs(F%d, 200)' % (i,i))
def a(i,l): return pari('c%d[%d+1]' % (i,l))
# check each eigenform mod 9 against l+1
import json
out = {}
for i in (1,2,3):
    rows=[]
    for l in pari('primes(200)'):
        l=int(l)
        if l==109: continue
        ai = a(i,l)
        s=str(ai)
        rows.append((l,s))
    out[i]=rows
with open('/tmp/coefs109.json','w') as f: json.dump(out,f)
print("saved")
for i in (1,2,3):
    print("=== form",i)
    for l,s in out[i][:25]:
        print(l,s)
