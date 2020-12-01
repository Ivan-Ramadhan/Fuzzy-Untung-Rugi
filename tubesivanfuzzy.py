import numpy as np
import matplotlib.pyplot as plt
class Fuzzy:
    memberOpRendah     = 0
    memberOpSedang     = 0
    memberOpTinggi     = 0

    memberPrRendah     = 0
    memberPrSedang     = 0
    memberPrTinggi     = 0
    
    memberPjRendah     = 0
    memberPjSedang     = 0 
    memberPjTinggi     = 0

    terbesarX          = 0
    terbesarY          = 0

    def __init__(self, operasional, produksi, penjualan):
        self.operasional    = operasional
        self.produksi       = produksi
        self.penjualan      = penjualan
    

    # Keanggotaan Operasional
    def anggota_operasional(self):
        cls = self.__class__

        # Bagian Rendah
        if (self.operasional <= 20):
            cls.memberOpRendah = 1
        else: 
            if(self.operasional < 50):
                cls.memberOpRendah = ((50 - self.operasional)/30)
            else:
                cls.memberOpRendah = 0
        
        # Bagian Sedang
        if((self.operasional <= 20) | (self.operasional >= 100 )):
            cls.memberOpSedang = 0
        else:
            if((self.operasional > 20) & (self.operasional < 50)):
                cls.memberOpSedang = ((self.operasional - 20)/30)
            else:
                if((self.operasional > 50) & (self.operasional < 100)):
                    cls.memberOpSedang = ((100 - self.operasional)/50)
                else:
                    cls.memberOpSedang = 1
        
        # Bagian Tinggi
        if(self.operasional <= 50):
            cls.memberOpTinggi = 0
        else:
            if((self.operasional > 50) & (self.operasional < 100)):
                cls.memberOpTinggi = ((self.operasional - 50)/50)
            else: 
                cls.memberOpTinggi = 1


    # Keanggotaan Produksi
    def anggota_produksi(self):
        cls = self.__class__

        # Bagian Rendah
        if (self.produksi <= 20):
            cls.memberPrRendah = 1
        else: 
            if(self.produksi < 50):
                cls.memberPrRendah = ((50 - self.produksi)/30)
            else:
                cls.memberPrRendah = 0
        
        # Bagian Sedang
        if((self.produksi <= 20) | (self.produksi >= 100 )):
            cls.memberPrSedang = 0
        else:
            if((self.produksi > 20) & (self.produksi < 50)):
                cls.memberPrSedang = ((self.produksi - 20)/30)
            else:
                if((self.produksi > 50) & (self.produksi < 100)):
                    cls.memberPrSedang = ((100 - self.produksi)/50)
                else:
                    cls.memberPrSedang = 1
        
        # Bagian Tinggi
        if(self.produksi <= 50):
            cls.memberPrTinggi = 0
        else:
            if((self.produksi > 50) & (self.produksi < 100)):
                cls.memberPrTinggi = ((self.produksi - 50)/50)
            else: 
                cls.memberPrTinggi = 1


    # Keanggotaan Penjualan
    def anggota_penjualan(self):
        cls = self.__class__

        # Bagian Rendah
        if (self.penjualan <= 40):
            cls.memberPjRendah = 1
        else: 
            if(self.penjualan < 100):
                cls.memberPjRendah = ((100 - self.penjualan)/60)
            else:
                cls.memberPjRendah = 0
        
        # Bagian Sedang
        if((self.penjualan <= 40) | (self.penjualan >= 200 )):
            cls.memberPjSedang = 0
        else:
            if((self.penjualan > 40) & (self.penjualan < 100)):
                cls.memberPjSedang = ((self.penjualan - 40)/60)
            else:
                if((self.penjualan > 100) & (self.penjualan < 200)):
                    cls.memberPjSedang = ((200 - self.penjualan)/100)
                else:
                    cls.memberPjSedang = 1
        
        # Bagian Tinggi
        if(self.penjualan <= 100):
            cls.memberPjTinggi = 0
        else:
            if((self.penjualan > 100) & (self.penjualan < 200)):
                cls.memberPjTinggi = ((self.penjualan - 100)/100)
            else: 
                cls.memberPjTinggi = 1      


    def inferensi(self):
        cls = self.__class__
        l = 0
        rule = []
        nilaikondisi = []
        kondisi= []
        nilaiOperasional = [cls.memberOpRendah, cls.memberOpSedang, cls.memberOpTinggi]
        nilaiProduksi    = [cls.memberPrRendah, cls.memberPrSedang, cls.memberPrTinggi]
        nilaiPenjualan   = [cls.memberPjRendah, cls.memberPjSedang, cls.memberPjTinggi]

        # print(nilaiOperasional)
        # print(nilaiProduksi)
        # print(nilaiPenjualan)

        print("\n\n-- Inferensi --")
        print("Rule")
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if((nilaiOperasional[i] > 0) & (nilaiProduksi[j] > 0 ) & (nilaiPenjualan[k] > 0) ):
                        #penetuan nilai min
                        if(min(nilaiOperasional[i], nilaiProduksi[j], nilaiPenjualan[k]) == nilaiOperasional[i]):
                            #nilaikondisi[l] = nilaiOperasional[i]
                            nilaikondisi.append(nilaiOperasional[i])
                        elif(min(nilaiOperasional[i], nilaiProduksi[j], nilaiPenjualan[k]) == nilaiProduksi[j]):
                            #nilaikondisi[l] = nilaiProduksi[j]
                            nilaikondisi.append(nilaiProduksi[j])
                        else:
                            #nilaikondisi[l] = nilaiPenjualan[k]
                            nilaikondisi.append(nilaiPenjualan[k])
                        
                        #penentuan Rule

                        #rule1
                        if((i==0) & (j ==0) & (k ==0) ):
                            kondisi += ["untung"]
                            rule = 1

                        #rule2
                        elif((i==0) & (j ==0) & (k==1) ):
                            kondisi += ["untung"]
                            rule = 2

                        #rule3
                        elif((i==0) & (j ==0) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 3

                        #rule4
                        elif((i==0) & (j ==1) & (k==0) ):
                            kondisi += ["rugi"]
                            rule = 4

                        #rule5
                        elif((i==0) & (j ==1) & (k==1) ):
                            kondisi += ["untung"]
                            rule = 5
 

                        #rule6
                        elif((i==0) & (j ==1) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 6

                        #rule7
                        elif((i==0) & (j ==2) & (k==0) ):
                            kondisi += ["rugi"]
                            rule = 7

                        #rule8
                        elif((i==0) & (j ==2) & (k==1) ):
                            kondisi += ["rugi"]
                            rule = 8

                        #rule9
                        elif((i==0) & (j ==2) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 9

                        #rule10
                        elif((i==1) & (j ==0) & (k==0) ):
                            kondisi += ["rugi"]
                            rule = 10 

                        #rule11
                        elif((i==1) & (j ==0) & (k==1) ):
                            kondisi += ["untung"]
                            rule = 11

                        #rule12
                        elif((i==1) & (j ==0) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 12
                            
                        #rule13
                        elif((i==1) & (j ==1) & (k==0) ):
                            kondisi += ["rugi"]
                            rule = 13
                            
                        #rule14
                        elif((i==1) & (j ==1) & (k==1) ):
                            kondisi += ["untung"]
                            rule = 14
                            
                        #rule15
                        elif((i==1) & (j ==1) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 15
                            
                        #rule16
                        elif((i==1) & (j ==2) & (k==0) ):
                            kondisi += ["rugi"]
                            rule = 16
                            
                        #rule17
                        elif((i==1) & (j ==2) & (k==1) ):
                            kondisi += ["rugi"]
                            rule = 17
                            
                        #rule18
                        elif((i==1) & (j ==2) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 18
                            
                        #rule19
                        elif((i==2) & (j ==0) & (k==0) ):
                            kondisi += ["rugi"]
                            rule = 19
                            
                        #rule20
                        elif((i==2) & (j ==0) & (k==1) ):
                            kondisi += ["rugi"]
                            rule = 20
                            
                        #rule21
                        elif((i==2) & (j ==0) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 21
                            
                        #rule22
                        elif((i==2) & (j ==1) & (k==0) ):
                            kondisi += ["rugi"]
                            rule = 22
                            
                        #rule23
                        elif((i==2) & (j ==1) & (k==1) ):
                            kondisi += ["rugi"]
                            rule = 23
                            
                        #rule24
                        elif((i==2) & (j ==1) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 24
                            
                        #rule25
                        elif((i==2) & (j ==2) & (k==0) ):
                            kondisi += ["rugi"]
                            rule = 25
                            
                        #rule26
                        elif((i==2) & (j ==2) & (k==1) ):
                            kondisi += ["rugi"]
                            rule = 26
                            
                        #rule27
                        elif((i==2) & (j ==2) & (k==2) ):
                            kondisi += ["untung"]
                            rule = 27
                        
                        else:
                            print("Tidak ditemukan")
                        # print(i,j,k)
                        
                        print("{} Ketika Opersional {} dan Produksi {} dan Penjualan {} maka hasil {} dengan nilai {}".format(rule,nilaiOperasional[i],nilaiProduksi[j],nilaiPenjualan[k],kondisi[l],nilaikondisi[l]))
                        
                        l += 1

        # menentukan nilai max
        
        
        for i in range(l):
            if(kondisi[i] == "rugi"):
                if(i == 0):
                    cls.terbesarX = nilaikondisi[i]
                
                else:
                    if(nilaikondisi[i] > cls.terbesarX):
                        cls.terbesarX = nilaikondisi[i]
            
            else:
                if(i == 0):
                    cls.terbesarY = nilaikondisi[i]
                
                else:
                    if(nilaikondisi[i] > cls.terbesarY):
                        cls.terbesarY = nilaikondisi[i]

        # print("\n")
        # print(kondisi)
        # print(nilaikondisi)
        if(cls.terbesarX > 0):
            print("\nNilai RUGI perusahaan \t = {}".format(cls.terbesarX))
        if(cls.terbesarY > 0):
            print("\nNilai UNTUNG perusahaan \t = {}".format(cls.terbesarY))                       


    def defuzzifikasi(self):
        cls = self.__class__
        sampel = 10
        hasilPembilang = 0
        hasilPenyebut = 0
        hasilDefuzzifikasi = 0
        titik_sampel = 0
        jumlah_sampelX = 0
        jumlah_sampelY = 0
        pengaliZ = []
        titik_sampelZ = []
        delta = 0
        k = 0

        pengaliX = cls.terbesarX
        pengaliY = cls.terbesarY
        delta    = 100/sampel
        titik_sampel += delta

        for i in range(sampel):
            if(titik_sampel <= 50):
                hasilPembilang += titik_sampel * pengaliX
                jumlah_sampelX += 1
            
            elif(titik_sampel > 80):
                hasilPembilang += titik_sampel * pengaliY
                jumlah_sampelY += 1
            
            elif ((titik_sampel > 50) & (titik_sampel < 80)):
                if(pengaliX > pengaliY):
                    titik_sampelZ += [titik_sampel]
                    pengaliZ += [round(((80 - titik_sampelZ[k])/30),2)]
                    hasilPembilang += titik_sampelZ[k] * pengaliZ[k]
                
                else:
                    titik_sampelZ += [titik_sampel]
                    pengaliZ += [round(((titik_sampelZ[k] - 50)/30),2)]
                    hasilPembilang += titik_sampelZ[k] * pengaliZ[k]

                k += 1

            titik_sampel += delta
        
        hasilPenyebut = (jumlah_sampelX * pengaliX) + (jumlah_sampelY * pengaliY )

        i = 0
        for i in range(k):
            hasilPenyebut += pengaliZ[i]
       
      
        # print("Hasil Pembilang = {}".format(hasilPembilang))
        # print("Hasil Penyebut = {}".format(hasilPenyebut))
        hasilDefuzzifikasi = hasilPembilang/hasilPenyebut
        print("\n\n-- Defuzzifikasi -- \n Jika nilai < 50 maka perusahaan rugi, Jika nilai > 50 maka perusahaan untung")
        print("Hasil Defuzzifikasi = {}".format(hasilDefuzzifikasi))
        


    def print(self):
        cls = self.__class__
        print("\n\n-- Fuzzifikasi --")
        print("OpRendah : {}".format(cls.memberOpRendah))
        print("OpSedang : {}".format(cls.memberOpSedang))
        print("OpTinggi : {}".format(cls.memberOpTinggi))

        print("\nPrRendah : {}".format(cls.memberPrRendah))
        print("PrSedang : {}".format(cls.memberPrSedang))
        print("PrTinggi : {}".format(cls.memberPrTinggi))

        print("\nPrRendah : {}".format(cls.memberPjRendah))
        print("PjSedang : {}".format(cls.memberPjSedang))
        print("PjTinggi : {}".format(cls.memberPjTinggi))


    def plot(self):
        cls = self.__class__
        x   = [0,20,50,100]
        x2  = [0,40,100,200]
        fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

        # plot figure operasional
        oprendah = np.concatenate((np.ones(2),np.zeros(2)))
        opsedang = np.concatenate((np.zeros(2),np.ones(1),np.zeros(1)))
        optinggi = np.concatenate((np.zeros(3),np.ones(1)))
        ax0.plot(x,oprendah,'b', linewidth=1.5, label='Rendah')
        ax0.plot(x,opsedang,'g', linewidth=1.5, label='Sedang')
        ax0.plot(x,optinggi,'r', linewidth=1.5, label='Tinggi')
        ax0.plot(self.operasional,cls.memberOpRendah,'ob',label = "{:.2f}".format(cls.memberOpRendah))
        ax0.plot(self.operasional,cls.memberOpSedang,'og',label = "{:.2f}".format(cls.memberOpSedang))
        ax0.plot(self.operasional,cls.memberOpTinggi,'or',label = "{:.2f}".format(cls.memberOpTinggi))
        ax0.set_title('Operational Cost')
        ax0.legend()

        # plot figure produksi
        prrendah = np.concatenate((np.ones(2),np.zeros(2)))
        prsedang = np.concatenate((np.zeros(2),np.ones(1),np.zeros(1)))
        prtinggi = np.concatenate((np.zeros(3),np.ones(1)))
        ax1.plot(x,prrendah,'b', linewidth=1.5, label='Rendah')
        ax1.plot(x,prsedang,'g', linewidth=1.5, label='Sedang')
        ax1.plot(x,prtinggi,'r', linewidth=1.5, label='Tinggi')
        ax1.plot(self.produksi,cls.memberPrRendah,'ob',label = "{:.2f}".format(cls.memberPrRendah))
        ax1.plot(self.produksi,cls.memberPrSedang,'og',label = "{:.2f}".format(cls.memberPrSedang))
        ax1.plot(self.produksi,cls.memberPrTinggi,'or',label = "{:.2f}".format(cls.memberPrTinggi))
        ax1.set_title('Production Cost')
        ax1.legend()

        # plot figure penjualan
        pjrendah = np.concatenate((np.ones(2),np.zeros(2)))
        pjsedang = np.concatenate((np.zeros(2),np.ones(1),np.zeros(1)))
        pjtinggi = np.concatenate((np.zeros(3),np.ones(1)))
        ax2.plot(x2,pjrendah,'b', linewidth=1.5, label='Rendah')
        ax2.plot(x2,pjsedang,'g', linewidth=1.5, label='Sedang')
        ax2.plot(x2,pjtinggi,'r', linewidth=1.5, label='Tinggi')
        ax2.plot(self.penjualan,cls.memberPjRendah,'ob',label = "{:.2f}".format(cls.memberPjRendah))
        ax2.plot(self.penjualan,cls.memberPjSedang,'og',label = "{:.2f}".format(cls.memberPjSedang))
        ax2.plot(self.penjualan,cls.memberPjTinggi,'or',label = "{:.2f}".format(cls.memberPjTinggi))    
        ax2.set_title('Sales Cost')
        ax2.legend()        

        for ax in (ax0, ax1, ax2):
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()
        
        plt.show()
        

operasional  = float(input("Masukkan biaya operasional (juta): "))
produksi     = float(input("Masukkan biaya produksi (juta): "))
penjualan    = float(input("Masukkan hasil penjualan (juta): "))

test = Fuzzy(operasional, produksi, penjualan)
test.anggota_operasional()
test.anggota_produksi()
test.anggota_penjualan()
test.print()
test.inferensi()
test.defuzzifikasi()
test.plot()
