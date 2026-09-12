import cmath, math
lam=2j*math.pi
def E(z): return lam*cmath.exp(z)
w0=complex(0.08803199956471025,0.014704204392486712)
orb=[w0]
z=w0
for i in range(60):
    z=E(z); orb.append(z)
print("pair (0,24) details:")
for i in [0,24]:
    print(i, f"({orb[i].real:.12f},{orb[i].imag:.12f})")
print("diff:", orb[24]-orb[0])
print("pair (1,25):", orb[25]-orb[1])
print("magnitudes 20..40:", [f"{abs(p):.4f}" for p in orb[20:41]])
# Is (0,24) close because orbit nearly preperiodic with preperiod 0 period 24? test orb[24+k] vs orb[k]
for k in range(6):
    print(k, abs(orb[24+k]-orb[k]))
# longer orbit to test recurrence of period 24
orb2=[w0]; z=w0
for i in range(120):
    z=E(z); orb2.append(z)
for q in [8,12,16,20,24,28,32]:
    ds=[abs(orb2[q+k]-orb2[k]) for k in range(4)]
    print(f"q={q}:", [f"{d:.2e}" for d in ds])
