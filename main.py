import customtkinter

root = customtkinter.CTk()
root.title("Финансы")
root.geometry("300x250")
root.resizable(False, False)

IncomeJanuary = 0
IncomeFebruary = 0
IncomeMarch = 0
IncomeApril = 0
IncomeMay = 0
IncomeJune = 0
IncomeJuly = 0
IncomeAugust = 0
IncomeSeptember = 0
IncomeOctober = 0
IncomeNovember = 0
IncomeDecember = 0

consumptionJanuary = 0
consumptionFebruary = 0
consumptionMarch = 0
consumptionApril = 0
consumptionMay = 0
consumptionJune = 0
consumptionJuly = 0
consumptionAugust = 0
consumptionSeptember = 0
consumptionOctober = 0
consumptionNovember = 0
consumptionDecember = 0

def reg():

    global IncomeJanuary
    global IncomeFebruary
    global IncomeMarch
    global IncomeApril
    global IncomeMay
    global IncomeJune
    global IncomeJuly
    global IncomeAugust
    global IncomeSeptember
    global IncomeOctober
    global IncomeNovember
    global IncomeDecember
    
    global consumptionJanuary
    global consumptionFebruary
    global consumptionMarch
    global consumptionApril
    global consumptionMay
    global consumptionJune
    global consumptionJuly
    global consumptionAugust
    global consumptionSeptember
    global consumptionOctober
    global consumptionNovember
    global consumptionDecember
    
    root.destroy()

    global name
    RegWindow = customtkinter.CTk()
    RegWindow.title(" ")
    RegWindow.geometry("250x180")
    RegWindow.resizable(False, False)

    def nextt():
        global IncomeJanuary
        global IncomeFebruary
        global IncomeMarch
        global IncomeApril
        global IncomeMay
        global IncomeJune
        global IncomeJuly
        global IncomeAugust
        global IncomeSeptember
        global IncomeOctober
        global IncomeNovember
        global IncomeDecember
        
        global consumptionJanuary
        global consumptionFebruary
        global consumptionMarch
        global consumptionApril
        global consumptionMay
        global consumptionJune
        global consumptionJuly
        global consumptionAugust
        global consumptionSeptember
        global consumptionOctober
        global consumptionNovember
        global consumptionDecember
    
        name = entry2.get()
        surname = entry.get()
        print(name)
        print(surname)
        RegWindow.destroy()
        
        def stat():
            global IncomeJanuary
            global IncomeFebruary
            global IncomeMarch
            global IncomeApril
            global IncomeMay
            global IncomeJune
            global IncomeJuly
            global IncomeAugust
            global IncomeSeptember
            global IncomeOctober
            global IncomeNovember
            global IncomeDecember
            
            global consumptionJanuary
            global consumptionFebruary
            global consumptionMarch
            global consumptionApril
            global consumptionMay
            global consumptionJune
            global consumptionJuly
            global consumptionAugust
            global consumptionSeptember
            global consumptionOctober
            global consumptionNovember
            global consumptionDecember
            
            def show_stats():
                global IncomeJanuary
                global IncomeFebruary
                global IncomeMarch
                global IncomeApril
                global IncomeMay
                global IncomeJune
                global IncomeJuly
                global IncomeAugust
                global IncomeSeptember
                global IncomeOctober
                global IncomeNovember
                global IncomeDecember
            
                global consumptionJanuary
                global consumptionFebruary
                global consumptionMarch
                global consumptionApril
                global consumptionMay
                global consumptionJune
                global consumptionJuly
                global consumptionAugust
                global consumptionSeptember
                global consumptionOctober
                global consumptionNovember
                global consumptionDecember
                
                if comboboxMonthStat.get() == 'Январь':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeJanuary))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionJanuary))
                    labelStat4.configure(text = "Итог: " + str(IncomeJanuary - consumptionJanuary))
            
                if comboboxMonthStat.get() == 'Февраль':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeFebruary))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionFebruary))
                    labelStat4.configure(text = "Итог: " + str(IncomeFebruary - consumptionFebruary))
            
                if comboboxMonthStat.get() == 'Март':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeMarch))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionMarch))
                    labelStat4.configure(text = "Итог: " + str(IncomeMarch - consumptionMarch))
                    
                if comboboxMonthStat.get() == 'Апрель':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeApril))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionApril))
                    labelStat4.configure(text = "Итог: " + str(IncomeApril - consumptionApril))
                    
                if comboboxMonthStat.get() == 'Май':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeMay))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionMay))
                    labelStat4.configure(text = "Итог: " + str(IncomeMay - consumptionMay))
                    
                if comboboxMonthStat.get() == 'Июнь':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeJune))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionJune))
                    labelStat4.configure(text = "Итог: " + str(IncomeJune - consumptionJune))
                    
                if comboboxMonthStat.get() == 'Июль':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeJuly))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionJuly))
                    labelStat4.configure(text = "Итог: " + str(IncomeJuly - consumptionJuly))
                    
                if comboboxMonthStat.get() == 'Август':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeAugust))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionAugust))
                    labelStat4.configure(text = "Итог: " + str(IncomeAugust - consumptionAugust))
                    
                if comboboxMonthStat.get() == 'Сентябрь':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeSeptember))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionSeptember))
                    labelStat4.configure(text = "Итог: " + str(IncomeSeptember - consumptionSeptember))
                    
                if comboboxMonthStat.get() == 'Октябрь':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeOctober))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionOctober))
                    labelStat4.configure(text = "Итог: " + str(IncomeSeptember - consumptionOctober))
                    
                if comboboxMonthStat.get() == 'Ноябрь':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeNovember))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionNovember))
                    labelStat4.configure(text = "Итог: " + str(IncomeNovember - consumptionNovember))
                    
                if comboboxMonthStat.get() == 'Декабрь':
                    labelStat2.configure(text = "Доходы за месяц: " + str(IncomeDecember))
                    labelStat3.configure(text = "Расходы за месяц: " + str(consumptionDecember))
                    labelStat4.configure(text = "Итог: " + str(IncomeDecember - consumptionDecember))
            
            stats = customtkinter.CTk()
            stats.title("Статистика")
            stats.geometry("300x250")
            stats.resizable(False, False)
            
            labelStat1 = customtkinter.CTkLabel(stats, text="Месяц:")
            labelStat1.pack()

            comboboxMonthStat = customtkinter.CTkComboBox(stats, values=["Январь", "Февраль", 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'])
            comboboxMonthStat.pack()
            
            labelStat2 = customtkinter.CTkLabel(stats, text="Доходы за месяц: ")
            labelStat2.pack()
            
            labelStat3 = customtkinter.CTkLabel(stats, text="Расходы за месяц: ")
            labelStat3.pack()
            
            labelStat4 = customtkinter.CTkLabel(stats, text="Итог: ")
            labelStat4.pack()

            btnShow = customtkinter.CTkButton(stats, text="Показать", command = show_stats)
            btnShow.pack()

            stats.mainloop()
            
            
        def add():
            global IncomeJanuary
            global IncomeFebruary
            global IncomeMarch
            global IncomeApril
            global IncomeMay
            global IncomeJune
            global IncomeJuly
            global IncomeAugust
            global IncomeSeptember
            global IncomeOctober
            global IncomeNovember
            global IncomeDecember
            
            global consumptionJanuary
            global consumptionFebruary
            global consumptionMarch
            global consumptionApril
            global consumptionMay
            global consumptionJune
            global consumptionJuly
            global consumptionAugust
            global consumptionSeptember
            global consumptionOctober
            global consumptionNovember
            global consumptionDecember
            
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Январь':
                IncomeJanuary = IncomeJanuary + int(entrySum.get())
                print(IncomeJanuary)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Февраль':
                IncomeFebruary = IncomeFebruary + int(entrySum.get())
                print(IncomeFebruary)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Март':
                IncomeMarch = IncomeMarch + int(entrySum.get())
                print(IncomeMarch)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Апрель':
                IncomeApril = IncomeApril + int(entrySum.get())
                print(IncomeApril)

            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Май':
                IncomeMay = IncomeMay + int(entrySum.get())
                print(IncomeMay)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Июнь':
                IncomeJune = IncomeJune + int(entrySum.get())
                print(IncomeJune)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Июль':
                IncomeJuly = IncomeJuly + int(entrySum.get())
                print(IncomeJuly)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Август':
                IncomeAugust = IncomeAugust + int(entrySum.get())
                print(IncomeAugust)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Сентябрь':
                IncomeSeptember = IncomeSeptember + int(entrySum.get())
                print(IncomeSeptember)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Октябрь':
                IncomeOctober = IncomeOctober + int(entrySum.get())
                print(IncomeOctober)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Ноябрь':
                IncomeNovember = IncomeNovember + int(entrySum.get())
                print(IncomeNovember)
                
            if combobox.get() == 'Доход' and comboboxMonth.get() == 'Декабрь':
                IncomeDecember = IncomeDecember + int(entrySum.get())
                print(IncomeDecember)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Январь':
                consumptionJanuary = consumptionJanuary + int(entrySum.get())
                print(consumptionJanuary)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Февраль':
                consumptionFebruary = consumptionFebruary + int(entrySum.get())
                print(consumptionFebruary)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Март':
                consumptionMarch = consumptionMarch + int(entrySum.get())
                print(consumptionMarch)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Апрель':
                consumptionApril = consumptionApril + int(entrySum.get())
                print(consumptionApril)

            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Май':
                consumptionMay = consumptionMay + int(entrySum.get())
                print(consumptionMay)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Июнь':
                consumptionJune = consumptionJune + int(entrySum.get())
                print(consumptionJune)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Июль':
                consumptionJuly = consumptionJuly + int(entrySum.get())
                print(consumptionJuly)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Август':
                consumptionAugust = consumptionAugust + int(entrySum.get())
                print(consumptionAugust)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Сентябрь':
                consumptionSeptember = consumptionSeptember + int(entrySum.get())
                print(consumptionSeptember)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Октябрь':
                consumptionOctober = consumptionOctober + int(entrySum.get())
                print(consumptionOctober)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Ноябрь':
                consumptionNovember = consumptionNovember + int(entrySum.get())
                print(consumptionNovember)
                
            if combobox.get() == 'Расход' and comboboxMonth.get() == 'Декабрь':
                consumptionDecember = consumptionDecember + int(entrySum.get())
                print(consumptionDecember)
        
        MainWindows = customtkinter.CTk()
        MainWindows.title("Финансы")
        MainWindows.geometry("300x400")
        MainWindows.resizable(False, False)
        
        labelHello = customtkinter.CTkLabel(MainWindows, text="Здравствуйте, " + name + ' ' + surname)
        labelHello.pack()
        
        labels = customtkinter.CTkLabel(MainWindows, text="Добавить:")
        labels.pack()
        
        combobox = customtkinter.CTkComboBox(MainWindows, values=["Доход", "Расход"])
        combobox.pack()

        labels2 = customtkinter.CTkLabel(MainWindows, text="Месяц:")
        labels2.pack()

        comboboxMonth = customtkinter.CTkComboBox(MainWindows, values=["Январь", "Февраль", 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'])
        comboboxMonth.pack()
        
        labels3 = customtkinter.CTkLabel(MainWindows, text="Сумма:")
        labels3.pack()
        
        entrySum = customtkinter.CTkEntry(MainWindows)
        entrySum.pack(padx=6, pady=6)
        
        btnAdd = customtkinter.CTkButton(MainWindows, text="Добавить", command = add)
        btnAdd.pack()
        
        btnStat = customtkinter.CTkButton(MainWindows, text="Показать статистику", command = stat)
        btnStat.pack(expand=True)

        MainWindows.mainloop()          

    label = customtkinter.CTkLabel(RegWindow, text="Введите свою фамилию")
    label.pack()
    
    entry = customtkinter.CTkEntry(RegWindow)
    entry.pack(padx=6, pady=6)

    label2 = customtkinter.CTkLabel(RegWindow, text="Введите свое имя")
    label2.pack()
    
    entry2 = customtkinter.CTkEntry(RegWindow)
    entry2.pack(padx=6, pady=6)
    
    btnNext = customtkinter.CTkButton(RegWindow, text="Продолжить", command = nextt)
    btnNext.pack()

    RegWindow.mainloop()

btnReg = customtkinter.CTkButton(root, text="Зарегистрироваться", command = reg)
btnReg.pack(expand=True)
 
root.mainloop()
