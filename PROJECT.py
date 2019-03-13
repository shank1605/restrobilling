from Tkinter import*
import random
def fun():
    roo.destroy()
    root=Tk()
    root.geometry("1600x800+0+0")   
    icon=PhotoImage(file="cake.gif")
    Label(root,image=icon).place(relx=.005,rely=0.01)
    ic=PhotoImage(file="cup.gif")
    Label(root,image=ic).place(x=1000,y=10)
    root.title("DUTCH FARM BAKERY")
    icon
    root.configure(background='black')
    Tops=Frame(root,width=1350,height=160,bd=14,relief="raise")
    Tops.pack(side=TOP)
    f1=Frame(root,width=900,height=650,bd=8,relief="raise")
    f1.pack(side=LEFT)
    
    f2=Frame(root,width=440,height=650,bd=8,relief="raise")
    f2.pack(side=RIGHT)

    f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
    f1a.pack(side=TOP)
    
    f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
    f2a.pack(side=BOTTOM)
    
    ft2=Frame(f2,width=440,height=450,bd=12,relief="raise")
    ft2.pack(side=TOP)
    
    fb2=Frame(f2,width=440,height=50,bd=16,relief="raise")
    fb2.pack(side=BOTTOM)
    
    flaa=Frame(f1a,width=400,height=330,bd=16,relief="raise")
    flaa.pack(side=LEFT)
    
    flab=Frame(f1a,width=400,height=330,bd=16,relief="raise")
    flab.pack(side=RIGHT)
    
    f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
    f2aa.pack(side=LEFT)
    
    f2ab=Frame(f2a,width=450,height=330,bd=14,relief="raise")
    f2ab .pack(side=RIGHT)
    
    Tops.configure(background='black')
     
    f1.configure(background='black')
    f2.configure(background='black')    
    lblInfo=Label(Tops,font=('Algerian',50,'bold'),text="DUTCH FARM BAKERY",bd=0)
    lblInfo.grid(row=0,column=0)
    root.configure(background="white")
    
    
    def CostofItem():
        Item1=float(E_RedVelvetCake.get())
        Item2=float(E_PineappleCake.get())
        Item3=float(E_CheeseCake.get())
        Item4=float(E_BlackForestCake.get())
        Item5=float(E_WhiteForestCake.get())
        Item6=float(E_ChocolateCake.get())
        Item7=float(E_VanillaCake.get())
        Item8=float(E_ButterscotchCake.get())
        
        Item9=float(E_VegSandwich.get())
        Item10=float(E_VegBurger.get())
        Item11=float(E_VegPizza.get())
        Item12=float(E_FrenchFries.get())
        Item13=float(E_IceTea.get())
        Item14=float(E_BlackcurrantShake.get())
        Item15=float(E_StrawberryShake.get())
        Item16=float(E_ColdCoffee.get())

       
    
        
    
    
    
    
        PriceofDrinks=(Item1*120)+(Item2*130)+(Item3*150)+(Item4*95)+(Item5*99)+(Item6*50)+(Item7*80)+(Item8*120)
        PriceofCakes=(Item9*400)+(Item10*500)+(Item11*350)+(Item12*200)+(Item13*1000)+(Item14*500)+(Item15*800)+(Item16*1200)
    
        DrinksPrice=str('%.2f'%(PriceofDrinks))
        CakesPrice=str('%.2f'%(PriceofCakes))
        CostofCakes.set(DrinksPrice)
        CostofDrinks.set(DrinksPrice)
        SC=str('%.2f'%(20))
        ServiceCharge.set(SC)
    
        SubTotalofITEMS=str('%.2f'%(PriceofDrinks+PriceofCakes+20))
        SUBTOTAL.set(SubTotalofITEMS)
    
        Tax=str((PriceofDrinks+PriceofCakes+20)*0.5)
        PAIDTAX.set(Tax)
    
        TT=((PriceofDrinks+PriceofCakes+20)*0.5 )
        TC=str('%.2f'%(PriceofDrinks+PriceofCakes+20+TT))
        TOTAL.set(TC)
    
    
    def Receipt():
     
         txtReceipt.delete("1.0",END)   
         x=random.randint(10908,500876)
         randomREf=str(x)
         
         
        
    
                
         txtReceipt.insert(END,'Items\t\t\t\t\t'+'Cost of Items\t')
         txtReceipt.insert(END,'\nRed Velvet Cake\t\t\t\t\t'+E_RedVelvetCake.get()+"\n")
         txtReceipt.insert(END,'Pineapple Cake\t\t\t\t\t'+E_PineappleCake.get()+"\n")
         txtReceipt.insert(END,'Cheese Cake\t\t\t\t\t'+E_CheeseCake.get()+"\n")
         txtReceipt.insert(END,'Black Forest Cake\t\t\t\t\t'+E_BlackForestCake.get()+"\n")
         txtReceipt.insert(END,'White Forest Cake\t\t\t\t\t'+E_WhiteForestCake.get()+"\n")
         txtReceipt.insert(END,'Chocolate Cake\t\t\t\t\t'+E_ChocolateCake.get()+"\n")
         txtReceipt.insert(END,'Vanilla Cake\t\t\t\t\t'+E_VanillaCake.get()+"\n")
         txtReceipt.insert(END,'Butterscotch Cake\t\t\t\t\t'+E_ButterscotchCake.get()+"\n")
         txtReceipt.insert(END,'Veg Sandwich\t\t\t\t\t'+E_VegSandwich.get()+"\n")
         txtReceipt.insert(END,'Veg Burger\t\t\t\t\t'+E_VegBurger.get()+"\n")
         txtReceipt.insert(END,'Veg Pizza\t\t\t\t\t'+E_VegPizza.get()+"\n")
         txtReceipt.insert(END,'French Fries\t\t\t\t\t'+E_FrenchFries.get()+"\n")
         txtReceipt.insert(END,'Ice Tea\t\t\t\t\t'+E_IceTea.get()+"\n")
         txtReceipt.insert(END,'Blackcurrant Shake\t\t\t\t\t'+E_BlackcurrantShake.get()+"\n")
         txtReceipt.insert(END,'Strawberry Shake\t\t\t\t\t'+E_StrawberryShake.get()+"\n")
         txtReceipt.insert(END,'Cold Coffee\t\t\t\t\t'+E_ColdCoffee.get()+"\n")
    
         txtReceipt.insert(END,'Cost of Drinks:\t\t\t'+CostofDrinks.get()+'\Tax Paid:'+PAIDTAX.get()+"\n")
         txtReceipt.insert(END,'Cost of Cakes:\t\t\t'+CostofCakes.get()+'\SubTotal:'+SUBTOTAL.get()+"\n")
         txtReceipt.insert(END,'Service Charge:\t\t\t'+ServiceCharge.get()+'\Total Cost:'+TOTAL.get()+"\n")
             
          
    
    
    def aExit():
        if aExit>0:
            root.destroy()
            return
    
    
        
    def reset():
        CostofDrinks.set("")
        CostofCakes.set("")
        ServiceCharge.set("")
        PAIDTAX.set ("")
        SUBTOTAL.set("")
        TOTAL.set("")
        txtReceipt.delete("1.0",END)
        
        E_RedVelvetCake.set("0")
        E_PineappleCake.set("0")
        E_CheeseCake.set("0")
        E_BlackForestCake.set("0")
        E_WhiteForestCake.set("0")
        E_ChocolateCake.set("0")
        E_VanillaCake.set("0")
        E_ButterscotchCake.set("0")
         
        E_VegSandwich.set("0")
        E_VegBurger.set("0")
        E_VegPizza.set("0")
        E_FrenchFries.set("0")
        E_IceTea.set("0")
        E_BlackcurrantShake.set("0")
        E_StrawberryShake.set("0")
        E_ColdCoffee.set("0")
        
       
    
     
       
    
        var1.set("0")
        var2.set("0")
        var3.set("0")
        var4.set("0")
        var5.set("0")
        var6.set("0")
        var7.set("0")
        var8.set("0")
        var9.set("0")
        var10.set("0")
        var11.set("0")
        var12.set("0")
        var13.set("0")
        var14.set("0")
        var15.set("0")
        var16.set("0")
    
       
    
    
          
    
    
    
       
    
    
    
        
        
    var1=IntVar( )
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()  
    var11=IntVar()
    var12=IntVar()
    var13=IntVar()
    var14=IntVar()
    var15=IntVar()  
    var16=IntVar()
    
    E_RedVelvetCake=StringVar()
    E_PineappleCake=StringVar()
    E_CheeseCake=StringVar()
    E_BlackForestCake=StringVar()
    E_WhiteForestCake=StringVar()
    E_ChocolateCake=StringVar()
    E_VanillaCake=StringVar()
    E_ButterscotchCake=StringVar()
    E_VegSandwich=StringVar()
    E_VegBurger=StringVar()
    E_VegPizza=StringVar()
    E_FrenchFries=StringVar()
    E_IceTea=StringVar()
    E_BlackcurrantShake=StringVar()
    E_StrawberryShake=StringVar()
    E_ColdCoffee=StringVar()
    CostofDrinks=StringVar()
    CostofCakes=StringVar()
    ServiceCharge=StringVar()
    PAIDTAX=StringVar()
    SUBTOTAL=StringVar()
    TOTAL=StringVar()
    
    
    
    
    E_RedVelvetCake.set("0")
    E_PineappleCake.set("0")
    E_CheeseCake.set("0")
    E_BlackForestCake.set("0")
    E_WhiteForestCake.set("0")
    E_ChocolateCake.set("0")
    E_VanillaCake.set("0")
    E_ButterscotchCake.set("0")
    E_VegSandwich.set("0")
    E_VegBurger.set("0")
    E_VegPizza.set("0")
    E_FrenchFries.set("0")
    E_IceTea.set("0")
    E_BlackcurrantShake.set("0")    
    E_StrawberryShake.set("0")
    E_ColdCoffee.set("0")

     
    var1.set("0") 
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")                           
    var7.set("0")
    var8.set("0")
    var9.set("0")       
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")
    
    
    RedVelvetCake=Checkbutton(flaa,text="RedVelvet Cake\t",variable=var1,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=0,sticky=W)
    
    PineappleCake=Checkbutton(flaa,text="Pineapple Cake\t",variable=var2,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=1,sticky=W)
    
    CheeseCake=Checkbutton(flaa,text="Cheese Cake\t",variable=var3,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=2,sticky=W)
    
    BlackForestCake=Checkbutton(flaa,text="BlackForest Cake\t",variable=var4,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=3,sticky=W)
    
    WhiteForestCake=Checkbutton(flaa,text="WhiteForest Cake\t",variable=var5,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=4,sticky=W)
    
    ChocolateCake=Checkbutton(flaa,text="Chocolate Cake\t",variable=var6,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=5,sticky=W)

    VanillaCake=Checkbutton(flaa,text="Vanilla Cake\t",variable=var7,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=6,sticky=W)
    
    ButterscotchCake=Checkbutton(flaa,text="Butterscotch Cake\t",variable=var8,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=7,sticky=W)
    
    
    
    
    VegSandwich=Checkbutton(flab,text="Veg Sandwich\t",variable=var9,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=0,sticky=W)
    
    VegBurger=Checkbutton(flab,text="Veg Burger\t",variable=var10,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=1,sticky=W)
        
    VegPizza=Checkbutton(flab,text="Veg Pizza\t",variable=var11,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=2,sticky=W)
    
    FrenchFries=Checkbutton(flab,text="French Fries\t",variable=var12,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=3,sticky=W)    
    
    IceTea=Checkbutton(flab,text="Ice Tea\t",variable=var13,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=4,sticky=W)
        
    BlackcurrantShake=Checkbutton(flab,text="Blackcurrant Shake\t",variable=var14,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=5,sticky=W)
    
    StrawbeeryShake=Checkbutton(flab,text="Strawberry Shake\t",variable=var15,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=6,sticky=W)
    
    ColdCoffe=Checkbutton(flab,text="Cold Coffe\t",variable=var16,onvalue=1,offvalue=0,font=('Harrington',18,'bold')).grid(row=7,sticky=W)
        
    txtRedVelvetCake=Entry(flaa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_RedVelvetCake,state=NORMAL)
    txtRedVelvetCake.grid(row=0,column=1)
    
    txtPineappleCake=Entry(flaa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_PineappleCake,state=NORMAL)
    txtPineappleCake.grid(row=1,column=1)
    
    txtCheeseCake=Entry(flaa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_CheeseCake,state=NORMAL)   
    txtCheeseCake.grid(row=2,column=1)   
    
    txtBlackForestCake=Entry(flaa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_BlackForestCake,state=NORMAL)
    txtBlackForestCake.grid(row=3,column=1)
    
    txtWhiteForestCake=Entry(flaa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_WhiteForestCake,state=NORMAL)
    txtWhiteForestCake.grid(row=4,column=1)
    
    txtChocolateCake=Entry(flaa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_ChocolateCake,state=NORMAL)
    txtChocolateCake.grid(row=5,column=1)
    
    txtVanillaCake=Entry(flaa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_VanillaCake,state=NORMAL)
    txtVanillaCake.grid(row=6,column=1)
    
    txtButterscotchCake=Entry(flaa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_ButterscotchCake,state=NORMAL)
    txtButterscotchCake.grid(row=7,column=1)



    


     
    
    
    
    txtVegSandwich=Entry(flab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_VegSandwich,state=NORMAL)
    txtVegSandwich.grid(row=0,column=1)
    txtVegBurger=Entry(flab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_VegBurger,state=NORMAL)
    txtVegBurger.grid(row=1,column=1)
    txtVegPizza=Entry(flab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_VegPizza,state=NORMAL)
    txtVegPizza.grid(row=2,column=1)
    txtFrenchFries=Entry(flab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_FrenchFries,state=NORMAL)
    txtFrenchFries.grid(row=3,column=1)
    txtIceTea=Entry(flab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_IceTea,state=NORMAL)
    txtIceTea.grid(row=4,column=1)
    txtBlackcurrantShake=Entry(flab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_BlackcurrantShake,state=NORMAL)
    txtBlackcurrantShake.grid(row=5,column=1)
    txtStrawberryShake=Entry(flab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_StrawberryShake,state=NORMAL)
    txtStrawberryShake.grid(row=6,column=1)
    txtColdCoffee=Entry(flab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_ColdCoffee,state=NORMAL)
    txtColdCoffee.grid(row=7,column=1)
    
    lblReceipt=Label(ft2,font=('arial',12,'bold'),text="Receipt",bd=2).grid(row=0,column=0,sticky=W)
    txtReceipt=Text(ft2,font=('arial',11,'bold'),bd=9,width=59,height=22,bg="white")
    txtReceipt.grid(row=1,column=0)

    
    
    
    
        

    lblServiceCharge=Label(f2aa,font=('arial',16,'bold'),text="Service Charge",bd=8)
    lblServiceCharge.grid(row=2,column=0,sticky=W)
    txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left',textvariable=ServiceCharge)
    txtServiceCharge.grid(row=2,column=1,sticky=W)
    
    
    
    
    
    
    lblPAIDTAX=Label(f2ab,font=('arial',16,'bold'),text="PAID TAX",bd=8)
    lblPAIDTAX.grid(row=0,column=0,sticky=W)
    txtPAIDTAX=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left',textvariable=PAIDTAX)
    txtPAIDTAX.grid(row=0,column=1,sticky=W)
    
    lblSUBTOTAL=Label(f2ab,font=('arial',16,'bold'),text="SUB TOTAL   ",bd=8)
    lblSUBTOTAL.grid(row=1,column=0,sticky=W)
    txtSUBTOTAL=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left',textvariable=SUBTOTAL)
    txtSUBTOTAL.grid(row=1,column=1,sticky=W)
    
    
    lblTOTAL=Label(f2ab,font=('arial',16,'bold'),text="TOTAL",bd=8)
    lblTOTAL.grid(row= 2,column=0,sticky=W)
    txtTOTAL=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left',textvariable=TOTAL)
    txtTOTAL.grid(row=2,column=1,sticky=W)
    
       
    
    
    
    
    
    
    btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('Viner Hand ITC',16,'bold'),width=5,text="Total",command=CostofItem).grid(row=0,column=0)
    btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('Viner Hand ITC',16,'bold'),width=5,text="Receipt",command=Receipt).grid(row=0,column=1)
    btnReset=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('Viner Hand ITC',16,'bold'),width=5,text="Reset",command=reset).grid(row=0,column=2)
    btnExit=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('Viner Hand ITC',16,'bold'),width=5,text="Exit",command=aExit).grid(row=0,column=3)
    
    
    
    
    
    
   
    
    
    
    mainloop()
    
roo=Tk()
roo.geometry("1600x800+0+0")
icon=PhotoImage(file="shake.gif")
Label(roo,image=icon).place(relx=.00,rely=.00)
l=Label(roo,image=icon,font="Ravie 80 bold",text="  DAILY DAIRY  ",compound=RIGHT,fg='BLUE',bg='black',bd=10)

roo.after(4000,fun)
mainloop()

