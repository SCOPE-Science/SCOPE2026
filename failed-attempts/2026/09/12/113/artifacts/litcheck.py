# Verify the exact fixed-point/lift identity at the singular value and check address conventions.
from mpmath import mp
mp.dps=50
lam=2*mp.pi*mp.mpc(0,1)
E=lambda z: lam*mp.e**z
print("E(0)=",E(0),"==lam:",E(0)==lam)
print("E(lam)=",E(lam),"diff=",abs(E(lam)-lam))
# strips: S_k = { (2k-1)pi < Im z < (2k+1)pi }; our lam=2pi i in S_1? (2*1-1)pi=pi < 2pi < 3pi yes k=1. singular value 0 in S_0.
# TM digits are 0/1, consistent.
# Check L_k fixed point equation: L_0(w)=log(w/lam); fixed: w=log(w/lam) -> E(w)=w i.e. periodic point, as expected.
# Distance from w0 to postsingular set:
w0=mp.mpc('0.08803199956471018304229084','0.01470420439248669282338643')
print("|w0|=",abs(w0),"|w0-lam|=",abs(w0-lam))
# Fast TM non-eventual-periodicity certificate: TM is cube-free => prove factor 010? Use known: if eventually periodic with preperiod a period q, then contains arbitrarily long cubes? Simpler: standard proof via cube-freeness + check first 3q symbols? We did computational check to q=40,p0<=20.
# For the WORKLOG we record morphism proof sketch: mu(0)=01,mu(1)=10, TM=mu^omega(0); overlap-free (Thue 1912) => not eventually periodic.
