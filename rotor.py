#inp- holds the value being passed into the rotor

def rotor(p1,p2,p3,inp,r1,r2,r3,refl):
    r1_inp=r1[0].index(inp)+1-p1                  #
    r1_op=r1[1][r1_inp]                           #finds the corresponding output to the input using the index from the previous line

    r2_inp=indexer(r2[0].index(r1_op)-p2+p1)
    r2_op=r2[1][r2_inp]

    r3_inp=indexer(r3[0].index(r2_op)-p3+p2)
    r3_op=r3[1][r3_inp]

    refl_inp=indexer(refl[0].index(r3_op)+p3-1)
    refl_op=refl[1][refl_inp]

    r3_inp=indexer(r3[0].index(refl_op)-p3+1)
    r3_ind=r3[1].index(r3[0][r3_inp])
    r3_op=r3[0][r3_ind]

    r2_inp=indexer(r2[0].index(r3_op)-p2+p3)
    r2_ind=r2[1].index(r2[0][r2_inp])
    r2_op=r2[0][r2_ind]

    r1_inp=indexer(r1[0].index(r2_op)+p2-p1)
    r1_ind=r1[1].index(r1[0][r1_inp])
    r1_op=r1[0][r1_ind]

    op_ind=indexer(r1[0].index(r1_op)+p1-1)
    op=r1[0][op_ind]


    return op


#function to prevent index from going out of bounds
def indexer(index):
    if index>25:
        index=index-26
    return index


