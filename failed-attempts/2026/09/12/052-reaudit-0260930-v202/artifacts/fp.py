import numpy as np, math

class LIF_FP:
    def __init__(self, tau_m=20.0, Vth=20.0, Vr=10.0, tref=2.0, Vlb=-30.0, N=900):
        self.tau_m=tau_m; self.Vth=Vth; self.Vr=Vr; self.tref=tref; self.Vlb=Vlb; self.N=N
        self.V=np.linspace(Vlb,Vth,N+1)
        self.dV=self.V[1]-self.V[0]
        self.iR=int(round((Vr-Vlb)/(Vth-Vlb)*N))
    def build(self, mu0, sig0):
        tau_m=self.tau_m; N=self.N; dV=self.dV; V=self.V
        D=sig0**2/(2*tau_m)
        a=(-V+mu0)/tau_m
        ae=0.5*(a[:-1]+a[1:])
        Pe=ae*dV/D
        def B(x):
            out=np.empty_like(x)
            small=np.abs(x)<1e-4
            big=~small
            out[small]=1-x[small]/2+x[small]**2/12
            xx=x[big]
            outb=np.empty_like(xx)
            m1=xx>50; m2=xx<-50; m3=~(m1|m2)
            outb[m1]=0.0
            outb[m2]=-xx[m2]
            x3=xx[m3]; outb[m3]=x3/(np.exp(x3)-1.0)
            out[big]=outb
            return out
        Bp=B(Pe); Bm=B(-Pe)
        c=D/dV
        n=N
        Lmat=np.zeros((n,n))  # div-J matrix: (J+ - J-)/dV ; true FP matrix F=-Lmat
        for i in range(n):
            if i<=N-2:
                Lmat[i,i]+=c*Bm[i]/dV
                Lmat[i,i+1]-=c*Bp[i]/dV
            else:
                Lmat[i,i]+=c*Bm[N-1]/dV
            if i==0:
                pass
            else:
                Lmat[i,i-1]-=c*Bm[i-1]/dV
                Lmat[i,i]+=c*Bp[i-1]/dV
        self.Lmat=Lmat; self.Bm=Bm; self.Bp=Bp; self.c=c
        return Lmat
    def stationary(self, mu0, sig0):
        self.build(mu0,sig0)
        n=self.N; dV=self.dV; iR=self.iR
        Lmat=self.Lmat
        # Lmat p = nu * s, s=delta at reset (1/dV)
        s=np.zeros(n); s[iR]=1.0/dV
        A=np.zeros((n+1,n+1)); A[:n,:n]=Lmat; A[:n,n]=-s
        A[n,:n]=dV; A[n,n]=self.tref
        b=np.zeros(n+1); b[n]=1.0
        x=np.linalg.solve(A,b)
        p=x[:n]; nu=x[n]
        self.p0=p; self.nu0=nu
        return p,nu
    def susceptibility(self, mu0, sig0, freqs_hz):
        p,nu=self.stationary(mu0,sig0)
        n=self.N; dV=self.dV; tau_m=self.tau_m; iR=self.iR
        pext=np.zeros(n+1); pext[:n]=p; pext[n]=0.0
        dp=np.gradient(pext, dV)[:n]
        f=-(1.0/tau_m)*dp  # forcing per unit mu1
        out=[]
        Lmat=self.Lmat
        I=np.eye(n)
        for f_hz in np.atleast_1d(freqs_hz):
            w=2*np.pi*f_hz/1000.0
            alpha=1.0/(1.0+1j*w*self.tref)
            s=np.zeros(n,dtype=complex); s[iR]=1.0/dV
            M=(1j*w)*I + Lmat.astype(complex)  # (iw - F) = iw + Lmat
            A=np.zeros((n+1,n+1),dtype=complex)
            A[:n,:n]=M; A[:n,n]=-alpha*s
            A[n,n-1]=self.c*self.Bm[self.N-1]
            A[n,n]=-1.0
            b=np.zeros(n+1,dtype=complex); b[:n]=f
            x=np.linalg.solve(A,b)
            out.append(x[n])
        return np.array(out)
