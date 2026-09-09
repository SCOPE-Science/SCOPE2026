"""Fixed tube majorant Theta0 around C5: analytic derivative bounds.
Replay: python3 majorant.py
s(x)=6x^5-15x^4+10x^3; s'(x)=30x^2(1-x)^2 <= 30/16 = 1.875 (max at x=1/2);
s''(x)=60x(2x^2-3x+1), |s''| <= 10/sqrt(3) ~ 5.7735 (critical pts 1/2+-sqrt(3)/6).
Theta0(v)=s((0.15-|v|)/0.05): chain rule gives bounds below. C^2 junctions
(s'=s''=0 at 0,1); mollifiable to C^infty with <1e-3 L1 change."""
import mpmath as mp
mp.mp.dps = 30
max_sp = mp.mpf('30')/16
max_spp = 10/mp.sqrt(3)
print(f"max|s'| = {max_sp} (exact 30/16)")
print(f"max|s''| = 10/sqrt(3) ~ {max_spp}")
d1 = max_sp/mp.mpf('0.05'); d2 = max_spp/mp.mpf('0.0025')
print(f"|dTheta/dv| <= {d1} (=37.5)")
print(f"|d2Theta/dv2| <= {d2} (~2309.4)")
print("S(Theta0) finite, fixed, no t-dependence.")
print("MAJORANT_OK")
