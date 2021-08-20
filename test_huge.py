'''
Description 
'''
import os

from eval.mots_eval.mots_common.io import load_seqmap


val = './eval/mots_eval/val_huge.seqmap'

seqmap, max_frames = load_seqmap(val)
print(seqmap)