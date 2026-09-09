"""Segmented/simple sieve regenerating all primes <= X=5e6 from code alone.
Committed scope: moduli 4,6; bound X=5000000; closed record predicate:
within-class consecutive gap strictly exceeding all previous within-class gaps.
"""
import json, os
X = 5000000
def sieve(n):
    bs = bytearray(b'\x01')*(n+1)
    bs[0]=bs[1]=0
    for i in range(2,int(n**0.5)+1):
        if bs[i]:
            bs[i*i:n+1:i]=b'\x00'*(((n-i*i)//i)+1)
    return bs
def main():
    is_prime = sieve(X)
    primes=[i for i in range(2,X+1) if is_prime[i]]
    os.makedirs("output/artifacts",exist_ok=True)
    with open("output/artifacts/prime_count.txt","w") as f:
        f.write(f"pi({X})={len(primes)}\n")
    def rec(mod_,res):
        flt=[p for p in primes if p%mod_==res]
        best=0; recs=[]
        for a,b in zip(flt,flt[1:]):
            if b-a>best: best=b-a; recs.append([b-a,a,b])
        return flt,recs
    R={}
    for q,r in [(4,1),(4,3),(6,1),(6,5)]:
        flt,recs=rec(q,r)
        R[f"{q}_{r}"]={"count":len(flt),"records":recs}
        with open(f"output/artifacts/filtered_{q}_{r}.txt","w") as f:
            f.write(" ".join(map(str,flt)))
    json.dump(R,open("output/artifacts/records.json","w"),indent=1)
    print("OK pi=",len(primes),"|",{k:(len(v["records"]),v["records"][-1]) for k,v in R.items()})
if __name__=="__main__": main()
