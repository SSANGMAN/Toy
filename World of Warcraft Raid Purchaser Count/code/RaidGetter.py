# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:20:50 2020

@author: PARK
"""

from tkinter import *
import tkinter as tk
import tkinter.messagebox
import datetime
import datetime

class Title:
    def __init__(self, where):
        self.buttonframe = Frame(where)
        
        self.label = Label(self.buttonframe, font = 2, text = "레이드 득자 처리 프로그램 ver 0.2(Test)", width = 40, height = 1)
        self.label.config(fg = 'blue', anchor = N)
        self.label.pack()
        
        self.dungeon = Label(self.buttonframe, text = "레이드 던전 선택", width = 15, height = 1)
        self.dungeon.config(fg = 'red', anchor = N)
        self.dungeon.pack(side = LEFT)
        
        self.buttonframe.pack(fill = X, anchor = N)
        self.button_mc = Button(self.buttonframe, text = "화산 심장부")
        self.button_mc.pack(side = LEFT, padx = 5, pady = 5)
        
        self.button_bw = Button(self.buttonframe, text = "검은 날개 둥지")
        self.button_bw.pack(side = LEFT, padx = 5, pady = 5)
        
        self.button_phase4 = Button(self.buttonframe, text = "줄구룹")
        self.button_phase4.pack(side = LEFT, padx = 5, pady = 5)
    
        self.button_phase5 = Button(self.buttonframe, text = "안퀴라즈")
        self.button_phase5.pack(side = LEFT, padx = 5, pady = 5)
        
        self.button_phase6 = Button(self.buttonframe, text = "낙스라마스")
        self.button_phase6.pack(side = LEFT, padx = 5, pady = 5)
        
        self.made_by = Label(self.buttonframe, text = "제작자 Github: @SSANGMAN /로크홀라 일산대표츄럴")
        self.made_by.pack(side = LEFT, pady = 10)
        
class Buttons:
    def __init__(self, button):
        self.buttonframe = Frame(button)
        self.buttonframe.pack(fill = X, anchor = N)
        
        self.get_name = Label(self.buttonframe, text = "득자명 : ", width = 6, height = 1)
        self.get_name.pack(side = LEFT, padx = 5)
        
        self.name = StringVar()
        self.who = Entry(self.buttonframe, textvariable = self.name)
        self.who.pack(side = LEFT, padx = 5)
        
        self.add_button = Button(self.buttonframe, text = "추가", width = 15, command = self.update)  # command
        self.add_button.pack(side = LEFT, padx = 5)
        
        self.delete_button = Button(self.buttonframe, text = "삭제", command = self.delete)
        self.delete_button.pack(side = LEFT, padx = 5)
        
        self.output_button = Button(self.buttonframe, text = "출력", command = self.output)
        self.output_button.pack(side = LEFT, padx = 5)
        
        self.reset_button = Button(self.buttonframe, text = "초기화", command = self.reset)
        self.reset_button.pack(side = LEFT, padx = 5)
        
        self.getter_list = Listbox(self.buttonframe, selectmode = 'single', width = 45, height = 10)
        self.getter_list.pack(side = BOTTOM, padx = 10, pady = 10)

        self.fixed_raider_button = Button(self.buttonframe, text = "공격대 인원 결정")
        self.fixed_raider_button.pack(side = LEFT, padx = 10)

    def update(self):
        self.getter_list.insert(END, self.name.get())
        tkinter.messagebox.showinfo("득자 추가", "득자 추가 완료!\n갱신 시간: {}".format(datetime.datetime.now()))
        
    def delete(self):
        items = self.getter_list.curselection()
        pos = 0
        
        for i in items:
            idx = int(i) - pos
            self.getter_list.delete(idx, idx)
            pos = pos + 1
            
        tkinter.messagebox.showinfo("득자 삭제", "득자 삭제 완료!\n갱신 시간: {}".format(datetime.datetime.now()))
        
    def reset(self):
        self.getter_list.delete(0, 'end')
        tkinter.messagebox.showinfo("초기화", "초기화 완료!\n초기화 시간: {}".format(datetime.datetime.now()))
        
    def output(self):
        output_list = self.getter_list.get(0, 'end')
        now = datetime.datetime.now()
        
        year = now.year
        month = now.month
        day = now.day

        with open('./result_example/{}{}{}.txt'.format(year, month, day), 'w') as f:

            f.write('득자: {}'.format(set(output_list)))
            f.write(', 총 {} 명'.format(len(set(output_list))))
            f.close()
            
        tkinter.messagebox.showinfo("출력", "출력 완료!\n출력 시간: {}\n 파일 경로를 확인해주세요!".format(datetime.datetime.now()))

def main():
    root = Tk()

    
    rg2 = Title(root)
    rg2 = Buttons(root)
    #rg3 = Getterlist(root)


    root.mainloop()

if __name__ == '__main__':
    main()