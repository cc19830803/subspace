from tkinter import SEL
import numpy as np
import math
class One:
    N = 100.0
    P = 50.0    
    __matrix_y =[]  
    __matrix_I =[]    #P*N的特征矩阵
    __matrix_yi = []
    Ip=[5]#P*1的特征向量
    def set(self,matrix_y,matrix_I,matrix_yi,Ip):
        self.__matrix_y = matrix_y
        self.__matrix_I = matrix_I  
        self.__matrix_yi = matrix_yi  
        self.Ip = Ip
        N = self.__matrix_y        
    def trace_YYH(self):
        y_y_h = np.conj(np.transpose(self.__matrix_y))  # �ȼ������Y��ת����ȡ����ת��
    
        trace = np.trace(self.__matrix_y*y_y_h)# ���㼣�������ھ���Խ���Ԫ��֮��
        return trace

    def get_matrix_R(self):
        n = 1/self.N
        y_y_h = np.conj(np.transpose(self.__matrix_y))  # �ȼ������Y��ת����ȡ����ת��
        print(self.__matrix_y)
        R = [x * n for x in self.__matrix_y * y_y_h]          
      #  R =  n* self.__matrix_y * y_y_h
        return R

#    -------------------------------------------


    def trace_1N_YYH(self):

        trace = np.trace(self.get_matrix_R())# ���㼣�������ھ���Խ���Ԫ��֮��
        return trace




    def get_rand(self):

        rand = 1/self.P*(self.trace_1N_YYH())

        return rand

    def get_yipixiu(self):
       # a = (1/(math.sqrt(self.P)))
       # yipixiu =(np.linalg.norm( get_matrix_R(N)-get_rand(P)*matrix_I),2 ,1 ,False ,True )          
        c2 = self.get_rand()        
        c1 =  np.multiply(self.Ip,c2)        
        cten = np.linalg.norm( self.get_matrix_R()-c1,2)    
            
        p1 = (1/(math.sqrt(self.P)))
        yipixiu = cten*p1    #norm(a, ord=None, axis=None, keepdims=False, check_finite=True)

        return yipixiu

    def get_alerfa(self):
        b =  1/(math.sqrt(self.P))    
    
        x =    self.get_yipixiu()           
        d = x * b    
        #a  = 1 / [x * b for x in self.get_yipixiu()]  
        c = 1 / d       
        #a = 1/((1/(math.sqrt(self.P)))*self.get_yipixiu())
        return c

    def get_sigam(self):
        sigam = self.get_alerfa()*self.trace_YYH()
        #print("sigam",sigam)
        return sigam

    def get_Py(self):
        cj = np.conj(np.transpose(self.__matrix_y))  
        si = self.get_sigam()   
        n___matrix_I = np.array(self.__matrix_I) 
        sy =  n___matrix_I *  si              
        # yy =  self.get_sigam()*self.__matrix_I      #[x * si for x in self.__matrix_I]   
        ny = np.transpose(self.__matrix_y)           
        cc = np.conj(ny)*self.__matrix_y + sy        

                 
        iv = np.linalg.inv(cc)
        Py = self.__matrix_y*iv*cj
        return Py   

    ## 2024��7��27�� SH  
    def get_Pyi(self):
        v = np.conj(np.transpose(self.__matrix_y)) * self.__matrix_y        
        Pyi = self.__matrix_yi * np.linalg.inv(v) * np.conj(np.transpose(self.__matrix_yi))        
        #Pyi = self.__matrix_yi * (1/(np.conj(np.transpose(self.__matrix_yi)) * self.__matrix_yi)) * np.conj(np.transpose(self.__matrix_yi))
        return Pyi
    def square_numbers(numbers):
    # ʹ�� map() �� lambda ��������ƽ��
        return list(map(lambda x: x ** 2, numbers))
    def get_SSMD(self):
        _py =   self.get_Py()
        _pyi = self.get_Pyi()      
        _py2 = _py**2   
        _pyi2 = _pyi**2
        _trace = np.trace(_py2) #np.trace(self.square_numbers(_py))
        _trace2 = np.trace(_pyi2) #np.trace(self.square_numbers(_pyi))
        _trace3  =  2 * np.trace(_py *_pyi)        
        SSMD =_trace  + _trace2 - _trace3
        return SSMD
    ## End    
if __name__ == "__main__":
    matrix_y = np.array( [[5.2,2.1,3.1],[2.1,2.1,3.1],[7.1,6.1,3.1]] ) #  
    matrix_I = np.array( [[5.2,2.1,3.1],[2.1,2.1,3.1],[7.1,6.1,3.1]] ) 
    matrix_yi = np.array( [[5.2,2.1,3.1]])
    one = One()
    one.N = 100;
    one.P = 50; 
    Ip1=3
    one.set(matrix_y,matrix_I,matrix_yi,Ip1)
    ## print("sssss", one.get_Py());
    print("sssss", one.get_SSMD());
    pass
# matrix_y = np.array( [[5.2,2.1,3.1],[2.1,2.1,3.1],[7.1,6.1,3.1]] ) #  
# matrix_I = np.array( [[5.2,2.1,3.1],[2.1,2.1,3.1],[7.1,6.1,3.1]] ) 
# matrix_yi = np.array( [[5.2,2.1,7.1]])
# one = One()
# one.set(matrix_y,matrix_I,matrix_yi)
# # print("sssss", one.get_Py());
# print("sssss", one.get_SSMD());



