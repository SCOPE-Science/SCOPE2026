#!/usr/bin/env python3
"""Generate or check the finite identifying-set certificate table."""
import csv
import io
import sys
from pathlib import Path
from verify import BALL, WORDS, selected

rows = [['code_mask','observed_vertex','identifying_set_bitmask_hex']]
for mask in (6949,6951,23333,23335):
    code = selected(mask)
    for word in WORDS:
        ids = BALL[word] & code
        bitmap = sum(1 << int(p,2) for p in ids)
        rows.append([str(mask), word, f'{bitmap:08x}'])
textbuf = io.StringIO()
writer = csv.writer(textbuf, lineterminator='\n')
writer.writerows(rows)
text = textbuf.getvalue()
path = Path(__file__).resolve().parent / 'signatures.csv'
if sys.argv[1:] == ['--check']:
    assert path.read_text(encoding='utf-8') == text
    print('SIGNATURE_TABLE_OK')
elif not sys.argv[1:]:
    path.write_text(text, encoding='utf-8')
    print('SIGNATURE_TABLE_WRITTEN')
else:
    raise SystemExit('usage: generate_signatures.py [--check]')
