import numpy as np
def run(N=4000,T=2500.0,dt=0.05,mu_ext=28.0,sig=5.0,JeffT=-600.0,Dmean=4.0,sigD=0.0,taus=2.0,seed=3):
    Jpsp=JeffT/N
    rng=np.random.default_rng(seed)
    tau_m=20.0; Vth=20.0; Vr=10.0; tref=2.0
    nT=int(T/dt)
    V=rng.uniform(Vr,Vth,N); I=np.zeros(N); ref=np.zeros(N)
    maxD=Dmean+10*max(sigD,0.01)+5; nbuf=int(maxD/dt)+2
    buf=[[] for _ in range(nbuf)]; step=0
    k=Dmean**2/max(sigD,1e-9)**2 if sigD>1e-9 else None
    th=sigD**2/Dmean if sigD>1e-9 else None
    pop=np.zeros(nT); sq=sig/np.sqrt(tau_m)*np.sqrt(dt)
    for t in range(nT):
        arr=buf[step%nbuf]
        if arr: I+=Jpsp*len(arr); buf[step%nbuf]=[]
        ref-=dt; ref[ref<0]=0
        active=ref<=0
        noise=rng.normal(size=N)*sq
        V[active]+= ((-(V[active])+mu_ext+I[active])/tau_m)*dt+noise[active]
        I-=I/taus*dt
        spk=np.where(active&(V>=Vth))[0]
        if len(spk)>0:
            pop[t]=len(spk); V[spk]=Vr; ref[spk]=tref
            if sigD<=1e-9: buf[(step+int(round(Dmean/dt)))%nbuf].extend([1]*len(spk))
            else:
                ds=rng.gamma(k,th,len(spk))
                for d in ds: buf[(step+int(round(d/dt)))%nbuf].append(1)
        step+=1
    return pop,dt
def spec(pop,dt,N):
    # population rate in Hz: r(t)=pop/(N*dt(ms))*1000
    r=pop/(N*(dt/1000.0))
    x=r-np.mean(r); w=np.hanning(len(x))
    X=np.fft.rfft(x*w); f=np.fft.rfftfreq(len(x),dt/1000.0)
    P=np.abs(X)**2/len(x)  # rate PSD-ish
    return f,P
import sys
for N in [1000,2000,4000]:
    for sigD in [0.0,2.0]:
        pop,dt=run(N=N,T=2500.0,sigD=sigD,seed=41)
        rate=np.sum(pop)/2.5/N
        f,P=spec(pop[int(500/0.05):],dt,N)
        med=np.median(P[(f>=30)&(f<=160)])
        m=(f>=55)&(f<=100); fpk=f[m][np.argmax(P[m])]
        print(f"N={N} sigD={sigD} rate={rate:.2f}Hz peak={fpk:.1f}Hz Pmax={np.max(P[m]):.3g} Pmed={med:.3g} ratio={np.max(P[m])/med:.1f}",flush=True)
