"""
Functions to generate sequences of data.
"""
import numpy as np

from utils import utils


def generate_fasta(length):
    """
    Generates a random FASTA sequence of <length>.
    
    Parameters:
    
        - length (int): the length of the FASTA sequence.
        
    Returns:
    
        - fasta (str)
    """
    
    aacodes = list(utils.aal1tol3.keys())
    
    return "".join(np.random.choice(aacodes, size=length))


def generate_3letter_list(length):
    """
    Generates a random protein sequence of <length>.
    
    Residue information given in amino-acid 3 letter code.
    
    Parameters:
    
        - lengh (int): the length of the FASTA sequence.
        
    Returns:
    
        - list (of 3 letter code)
    """
    
    aacodes = list(utils.aal3tol1.keys())
    
    return np.random.choice(aacodes, size=length).tolist()
