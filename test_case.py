import unittest
import matrix as m

class Testmatrix(unittest.TestCase):
    
    def test_eigvalue_a(self):
        a = [[2,0],[0,-3]]
        matrix = m.martix_2x2(a)
        eig = matrix.eig()
        eigv = matrix.eigv()
        excepted = (2,-3)
        self.assertAlmostEqual(excepted[0],eig[0])
        self.assertAlmostEqual(excepted[1],eig[1])
        vexcepted = [[1,0],[0,1]]
        self.assertEqual(vexcepted,eigv)
    
    def test_b(self):
        b = [[1,6],[5,2]]
        matrix = m.martix_2x2(b)
        eig = matrix.eig()
        eigv = matrix.eigv()
        excepted = (7,-4)
        self.assertAlmostEqual(excepted[0],eig[0])
        self.assertAlmostEqual(excepted[1],eig[1])
        vexcepted = [[1,1],[-1.2,1]]
        self.assertEqual(vexcepted,eigv)
        

    def test_c(self):
        c = [[7,2],[-4,1]]
        matrix = m.martix_2x2(c)
        eig = matrix.eig()
        eigv = matrix.eigv()
        excepted = (5,3)
        self.assertAlmostEqual(excepted[0],eig[0])
        self.assertAlmostEqual(excepted[1],eig[1])
        vexcepted = [[-1,1],[-0.5,1]]
        self.assertEqual(vexcepted,eigv)
    
    def test_v(self):
        v = [[1,1],[1,1]]
        matrix = m.martix_2x2(v)
        eig = matrix.eig()
        eigv = matrix.eigv()
        excepted = (2,0)
        self.assertAlmostEqual(excepted[0],eig[0])
        self.assertAlmostEqual(excepted[1],eig[1])
        vexcepted = [[1,1],[-1,1]]
        self.assertEqual(vexcepted,eigv)
        
    def test_w(self):
        w = [[2,1],[0,2]]
        matrix = m.martix_2x2(w)
        eig = matrix.eig()
        eigv = matrix.eigv()
        excepted = (2,2)
        self.assertAlmostEqual(excepted[0],eig[0])
        self.assertAlmostEqual(excepted[1],eig[1])
        vexcepted = [[1,0],[1,0]]
        self.assertEqual(vexcepted,eigv)
    
    
    def test_x(self):
        x = [[3,1],[-1,1]]
        matrix = m.martix_2x2(x)
        eig = matrix.eig()
        eigv = matrix.eigv()
        excepted = (2,2)
        self.assertAlmostEqual(excepted[0],eig[0])
        self.assertAlmostEqual(excepted[1],eig[1])
        vexcepted = [[-1,1],[-1,1]]
        self.assertEqual(vexcepted,eigv)
    
    
if __name__ == '__main__':
    unittest.main()