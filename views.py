"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template , Flask , request , url_for , redirect
from FlaskWebProject1 import app
import time

def Twos_comp(M):
    M_ = []
    j = len(M)
    for i in range(len(M)):
        
        if M[i] == 0:
            M_.append(1)
        elif M[i] == 1:
            M_.append(0)
    M_ = lst_to_srt(M_)
    M_ = bin(int(M_,2) + 1)[2:]
    while len(M_) < j:
        M_ = '0' + M_
    M_ = str_to_lsd(M_)
    return M_
def str_to_lsd(M_):
    l =[]
    for i in M_:
        l.append(int(i))
    return l
def lst_to_srt(lst):
    i = ""
    for j in lst:
        i += str(j)
    return i
def tobinry(val):
    lst = []
    if val >= 0:
        bit = bin(val)[2:]
        for i in bit:
            lst.append(int(i))
        return lst
        
    else:
        bit = bin(val)[3:]
        for i in bit:
            lst.append(int(i))

        return lst
def addition(A,M):
    count1 = len(A)

    A = lst_to_srt(A)
    
    M = lst_to_srt(M)
    A = bin(int(A,2)+int(M,2))[2:]
  
    count2 = len(A)
   
    A = A[(count2-count1):]
 
    A = str_to_lsd(A)
    if len (A) < len(M):
        for i in range(len(M) - len(A)):
            A = [0] + A

    
    return A
def Rshift(A,Q,Q_):
    tempA = []
    tempQ = []
    
    Q_ = [Q[-1]]

    #for Q
    for i in range(2,len(A)+1):
        tempQ.append(Q[-i])

    tempQ.reverse()
    tempQ = [A[-1]] + tempQ
    Q = tempQ
    tempQ = []



    for i in range(2,len(A)+1):
 
        tempA.append(A[-i])
    tempA.reverse()
    tempA = [A[0]] + tempA
    A = tempA
    tempA = []
    return A,Q,Q_
def lsft(C,A,Q):
 
    C = [A[0]]

    #for A
    for i in range(len(A)-1):
        A[i] = A[i+1]
    A[-1] = Q[0]

    #for Q
    for i in range(len(A)-1):
        Q[i] = Q[i+1]
    Q[-1] =  ""

    return C,A,Q
def resadd(C,A,M_):
    ac = C+A
    ac = addition(ac,M_)
    c = [ac[0]]
    del ac[0]
    return  c , ac
def lst_to_dec(lst):
    bi = lst_to_srt(lst)

    bi = int(bi,2)

    return bi

def Booths(a,b):
    mulcant = int(a) #int(input("multiplicant > "))
    mulpler = int(b) #int(input("multiplier   > "))

    final_cycle = []
    final_a = []
    final_Q = []
    final_q = []
    final_steps = []
    



    M = tobinry(mulcant)
    Q = tobinry(mulpler)
    A = []
    q = [0]
            
    #organise:
    if len(M) < 16:
        for i in range(16-len(M)):
            M = [0] + M
    if len(Q) < 16:
        for i in range(16-len(Q)):
            Q = [0] + Q
   
      
    if len(M) < len(Q):
        for i in range(len(M),len(Q)):
            M  = [0] + M
    elif len(M) > len(Q):
        for i in range(len(Q),len(M)):
            Q = [0] + Q
    for i in range(len(M)):
        A.append(0)
    M_ = Twos_comp(M)
    #all done A,M,2'sM,Q,Q-1

   


    final_a.append(A)
    final_Q.append(Q)
    final_q.append(q)
    final_steps.append(" Start ")
    final_cycle.append(" ")
    
   



    i = 0

    while i < len(Q):
        
        #final_cycle.append(i)


        if Q[-1] == 1 and q[0] == 0:
            #A = A + 2's m
            final_cycle.append(i)
            A = addition(A,M_)

            
            final_a.append(A)
            final_Q.append(Q)
            final_q.append(q)
            final_steps.append("10:A = A - M")
            
            final_cycle.append(i)
            A,Q,q = Rshift(A,Q,q)
            final_a.append(A)
            final_Q.append(Q)
            final_q.append(q)
            final_steps.append("Right shift")
       
            
           
        elif Q[-1] == 0 and q[0] == 1:
            #A = A + m
    
      
            A = addition(A,M)
            final_cycle.append(i)
            final_a.append(A)
            final_Q.append(Q)
            final_q.append(q)
            final_steps.append("01:A = A + M")
      
      
            final_cycle.append(i)
            A,Q,q = Rshift(A,Q,q)
            
            final_a.append(A)
            final_Q.append(Q)
            final_q.append(q)
            final_steps.append("Right shift")
          
 
       
   
        else:
           
      
            A,Q,q = Rshift(A,Q,q)
            final_steps.append("00 or 11 : Right shift")
            final_cycle.append(i) 
            final_a.append(A)
            final_Q.append(Q)
            final_q.append(q)
           
          
       

        i += 1
    
        
    fff = A+Q
    #if len(fff) > 8:
    #    for i in range(1,9):
    #        fin_lst.append(fff[-i])
    

   
   
    if mulcant < 0 and mulpler < 0:
        final_cycle.append(" ")
        final_steps.append("Your answer")
        final_a.append(lst_to_dec(fff))
        final_Q.append(fff)
        final_q.append("=")
       
    elif mulcant < 0 or mulpler < 0:
        neg_ans = Twos_comp(fff)
        final_cycle.append(" ")
        final_a.append(-lst_to_dec(fff))
        final_steps.append("Your answer")
        final_q.append("=")
     
        final_Q.append(neg_ans)
     
    else:
        final_cycle.append(" ")
        final_steps.append("Your answer")
        final_a.append(lst_to_dec(fff))
        final_Q.append(fff)
        final_q.append("=")
    return final_cycle ,final_a , final_Q ,final_q ,final_steps
def Restoring(a,b): 


  
    divdnt = int(a) #int(input("Divident> "))
    divsor = int(b) #(input("Divisor > "))
   
    M = tobinry(divsor)
    Q = tobinry(divdnt)
    A = []
    C = [0]

    final_cycle = []
    final_a = []
    final_Q = []
    final_c= []
    final_steps = []
    def store(c,C,A,Q,s):
        final_cycle.append(c)
        final_c.append(C)
        final_a.append(A)
        final_Q.append(f'{Q}')
        final_steps.append(s)



    #organise:
    if len(M) < 16:
        for i in range(16-len(M)):
            M = [0] + M
    if len(Q) < 16:
        for i in range(16-len(Q)):
            Q = [0] + Q
   
      
    if len(M) < len(Q):
        for i in range(len(M),len(Q)):
            M  = [0] + M

    elif len(M) > len(Q):
        for i in range(len(Q),len(M)):
            Q = [0] + Q
    M  = [0] + M
    for i in range(len(M)-1):
        A.append(0)
    M_ = Twos_comp(M)
    
    #all done A,M,2'sM,Q,Q-1
    store("",C,A,Q,"Start")

    i = 0
    while i < len(Q):
   
       
        C,A,Q = lsft(C,A,Q)
        store(i,C,A,Q,"Left Shift")

        
        C,A = resadd(C,A,M_)
        store(i,C,A,Q,"CA = CA - M")


        
        if C[0] == 1:
                Q[-1] = 0
          
             
                store(i,C,A,Q,"C  -►•-  Q[-1]")
                
                #restore
                C,A = resadd(C,A,M)
                store(i,C,A,Q,"CA = CA + M")
     
        elif C[0] == 0:
                Q[-1] = 1

                store(i,C,A,Q,"C  -►•-  Q[-1]")

        i += 1

    #check if the remiander is 0 nand divdent or divsor is 0

    quoti = int(lst_to_dec(Q))
    remin = int(lst_to_dec(A))

    if divdnt < 0  and divsor < 0 :
        store('',quoti,Q,"=","Quotient")
        store('',remin,A,"=",'Remiander')
    
    elif divdnt < 0  or divsor < 0 :
        
        Q = Twos_comp(Q)
            
        store('',-quoti,Q,"=","Quotient")
        store('',remin,A,"=",'Remiander')
    
    else:
        store('',quoti,Q,"=","Quotient")
        store('',remin,A,"=",'Remiander')

    return final_cycle ,final_a , final_Q ,final_c ,final_steps
def Non_restoring(a,b):      

    divdnt = int(a) #int(input("Divident> "))
    divsor = int(b) #(input("Divisor > "))
    M = tobinry(divsor)
    Q = tobinry(divdnt)
    A = []
    C = [0]

    final_cyc =[]
    final_c =[]
    final_a =[]
    final_q =[]
    final_stp =[]

    
    
    #organise:
    if len(M) < 16:
        for i in range(16-len(M)):
            M = [0] + M
    if len(Q) < 16:
        for i in range(16-len(Q)):
            Q = [0] + Q
   
   
    if len(M) < len(Q):
        for i in range(len(M),len(Q)):
            M  = [0] + M

    elif len(M) > len(Q):
        for i in range(len(Q),len(M)):
            Q = [0] + Q
    M  = [0] + M
    
    for i in range(len(M)-1):
        A.append(0)
    
         
    M_ = Twos_comp(M)

    #all done A,M,2'sM,Q,Q-1

    def store(cyc,C,A,Q,stp):
        final_cyc.append(cyc)
        final_c  .append(C)
        final_a  .append(A)
        final_q.append(f'{Q}')
        final_stp.append(stp)
    
    store("",C,A,Q,"start")
    
    
  
    i = 0
    while i < len(Q):
      
    
        if C[0] == 0:
         
            store(i,C,A,Q,f'C is,{C[0]}')
        
            
            C,A,Q = lsft(C,A,Q)
            store(i,C,A,Q,'Left shift')
         
    
            
            C,A = resadd(C,A,M_)
            store(i,C,A,Q,'CA = CA - M')
      
      

   
            if C[0] == 0 :
                Q[-1] = 1
            else:
                Q[-1] = 0
       
            store(i,C,A,Q,'C -►•- Q[-1]')

       
        elif C[0] == 1:
            
 
            store(i,C,A,Q,f'C is:{C[0]}')
            
            C,A,Q = lsft(C,A,Q)
            store(i,C,A,Q,'Left shift')
   
            
            
            C,A = resadd(C,A,M)
            store(i,C,A,Q,'CA = CA + M')
  
            
            if C[0] == 0 :
                Q[-1] = 1
            else:
                Q[-1] = 0
         
            store(i,C,A,Q,'C -►•- Q[-1]')
  
        i += 1

    if C[0] == 1:
        C,A = resadd(C,A,M)
  

      
     
    quoti = int(lst_to_dec(Q))
    remin = int(lst_to_dec(A))

    if divdnt < 0  and divsor < 0 :
        store('',quoti,Q,"=","Quotient")
        store('',remin,A,"=",'Remiander')
    
    elif divdnt < 0  or divsor < 0 :
        
        Q = Twos_comp(Q)
            
        store('',-quoti,Q,"=","Quotient")
        store('',remin,A,"=",'Remiander')
    
    else:
        store('',quoti,Q,"=","quotient")
        store('',remin,A,"=",'remiander')
    
    return final_cyc ,final_a , final_q ,final_c ,final_stp
def lru(s, capacity):
    # print("Enter the number of frames: ", end="")
    # capacity = int(input())
    solList = []
    f, st, fault, pf = [], [], 0, 'No'
    # print("Enter the reference string: ", end="")
    l = list(map(int, s.strip().split(',')))
    # print("\nString|Frame →\t", end='')
    L1 = ["String|Frame →"]
    L2 = []
    L3 = []
    for i in range(capacity):
        # print(i, end=' ')
        L1.append(i)
    # solList.append(f'String|Frame →  {temp}  Fault')
    # print("Fault\n   ↓\n")
    L1.append("Fault")
    L3.append(L1)
    for i in l:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
                st.append(len(f) - 1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            pf = 'Yes'
            fault += 1
        else:
            st.append(st.pop(st.index(f.index(i))))
            pf = 'No'
        # print("   %d\t\t" % i, end='')
        L2.append(i)
        for x in f:
            # print(x, end=' ')
            L2.append(x)
        for x in range(capacity - len(f)):
            # print(' ', end=' ')
            L2.append(" ")
        # print(" %s" % pf)
        L2.append(pf)
        L3.append(L2)
        L2 = []
    solList.append(f'Total requests: {(len(l))}')
    solList.append(f'Total Page Faults: {fault}')
    solList.append(f'Fault Rate: {((fault / len(l)) * 100)}')
    solList.append(f'Total Page Hit: {(len(s) - fault)}')
    solList.append(f'Hit Rate: {(((len(l) - fault) / len(l)) * 100)}')
    L3.append(solList)
    # print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(s), fault, (fault / len(s)) *
    # 100)) return fault
    return L3

    return solList
def Fifo(s, capacity):
    # print("Enter the number of frames: ", end="")
    # capacity = int(input())
    f, fault, top, pf = [], 0, 0, 'No'
    # print("Enter the reference string: ", end="")
    l = list(map(int, s.strip().split(',')))
    # print("\nString|Frame →\t", end='')
    L1 = ["String|Frame →"]
    L2 = []
    solList = []
    L3 = []

    for i in range(capacity):
        # print(i, end=' ')
        L1.append(i)
    # print("Fault\n   ↓\n")
    L1.append("Fault")
    L3.append(L1)
    for i in l:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
            else:
                f[top] = i
                top = (top + 1) % capacity
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        # print("   %d\t\t" % i, end='')
        L2.append(i)
        for x in f:
            # print(x, end=' ')
            L2.append(x)
        for x in range(capacity - len(f)):
            # print(' ', end=' ')
            L2.append(" ")
        # print(" %s" % pf)
        L2.append(pf)
        L3.append(L2)
        L2 = []
    solList.append(f'Total requests: {(len(l))}')
    solList.append(f'Total Page Faults: {fault}')
    solList.append(f'Fault Rate: {((fault / len(l)) * 100)}')
    solList.append(f'Total Page Hit: {(len(s) - fault)}')
    solList.append(f'Hit Rate: {(((len(l) - fault) / len(l)) * 100)}')
    L3.append(solList)
    # print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(l), fault, (fault / len(l)) *
    # 100)) return fault
    return L3
def optimal(s, capacity):
    # print("Enter the number of frames: ", end="")
    # capacity = int(input())
    solList = []
    f, fault, pf = [], 0, 'No'
    # print("Enter the reference string: ", end="")
    l = list(map(int, s.strip().split(',')))    # print("\nString|Frame →\t", end='')
    L1 = ["String|Frame →"]
    L2 = []
    solList = []
    L3 = []
    for i in range(capacity):
        # print(i, end=' ')
        L1.append(i)
    # print("Fault\n   ↓\n")
    L1.append("Fault")
    L3.append(L1)
    occurance = [None for i in range(capacity)]
    for i in range(len(l)):
        if l[i] not in f:
            if len(f) < capacity:
                f.append(l[i])
            else:
                for x in range(len(f)):
                    if f[x] not in l[i + 1:]:
                        f[x] = l[i]
                        break
                    else:
                        occurance[x] = l[i + 1:].index(f[x])
                else:
                    f[occurance.index(max(occurance))] = l[i]
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        # print("   %d\t\t" % s[i], end='')
        L2.append(i)
        for x in f:
            # print(x, end=' ')
            L2.append(x)
        for x in range(capacity - len(f)):
            # print(' ', end=' ')
            L2.append(" ")
        # print(" %s" % pf)
        L2.append(pf)
        L3.append(L2)
        L2 = []
    solList.append(f'Total requests: {(len(l))}')
    solList.append(f'Total Page Faults: {fault}')
    solList.append(f'Fault Rate: {((fault / len(l)) * 100)}')
    solList.append(f'Total Page Hit: {(len(s) - fault)}')
    solList.append(f'Hit Rate: {(((len(l) - fault) / len(l)) * 100)}')
    L3.append(solList)
    # print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(s), fault, (fault / len(s)) * 100))
    # return fault
    return L3




















@app.route("/")
@app.route('/home')
def home():


    return render_template('home.html',title='Home Page')

@app.route('/booth',methods = ["POST","GET"])
def booth():
    if request.method == "POST":
        
        a = request.form["num1"]
        b = request.form["num2"]
        Cyc,a,Q,q,step = Booths(a,b)
      
        return render_template('booth.html',len = len(Q)-1,Cyc = Cyc , A =a , Q = Q ,q =q, steps = step)
    else:
        return render_template('boothh.html')
   
@app.route('/restoring',methods = ["POST","GET"])
def resto():
     if request.method == "POST":
        a = request.form["num1"]
        b = request.form["num2"]
        Cyc ,A , Q ,C,steps = Restoring(a,b)
        return render_template('restoring.html',len = len(Q)-2,Cyc = Cyc ,A = A , Q  = Q,C = C,steps = steps)
     else:
         return render_template('resto.html')
    
@app.route('/nonrestoring',methods = ["POST","GET"])
def nonrestoring():
     if request.method == "POST":
        a = request.form["num1"]
        b = request.form["num2"]
        Cyc ,A , Q ,C,steps = Non_restoring(a,b)
        return render_template('nonrestoringC.html',len = len(Q)-2,Cyc = Cyc ,A = A , Q  = Q,C = C,steps = steps,n1 =a, n2=b)
     else:
         return render_template('nonrestoringH.html')

@app.route('/lru',methods=["POST","GET"])
def Lru():
    if request.method == "POST":
        fram = int(request.form["num1"])
        string = request.form["num2"]
        l = lru(string,fram)
        ref_string = []
        for i in range(len(l)):
            ref_string.append(l[i][0])
        print(len(l[0]),len(l))#(len,l_len)
        return render_template('lruC.html',  ref_string = ref_string , len = len(l[0]), l_len=len(l), l = l)
   
    else:
        return render_template('lru.html')

@app.route('/fifo',methods=["POST","GET"])
def fifo():
    if request.method == "POST":
        fram = int(request.form["num1"])
        string = request.form["num2"]
        l = Fifo(string,fram)
        ref_string = []
        for i in range(len(l)):
            ref_string.append(l[i][0])
        print(len(l[0]),len(l))#(len,l_len)
        return render_template('fifoC.html',  ref_string = ref_string , len = len(l[0]), l_len=len(l), l = l)
    else:
        return render_template('fifo.html')


       

            








@app.route('/optimal',methods=["POST","GET"])
def optim():
    if request.method == "POST":
        fram = int(request.form["num1"])
        string = request.form["num2"]
        l = optimal(string,fram)
        ref_string = []
        for i in range(len(l)):
            ref_string.append(l[i][0])
        print(len(l[0]),len(l))#(len,l_len)
        return render_template('optimC.html',  ref_string = ref_string , len = len(l[0]), l_len=len(l), l = l)
    else:
        return render_template('optimal.html')


if __name__ == "__main__":
    app.run(debug = True)