#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gtk import RESPONSE_OK
import time
import webbrowser

from baseaction import BaseAction

class Add(BaseAction):    
    def __init__(self, gui):
        self.update_list = True
        self.__gui = gui

    def do(self, planned_broadcasts):
        if self.__gui.dialog_planning.run_new() == RESPONSE_OK:           
            broadcast, datetime, station = self.__gui.dialog_planning.get_values()
            planned_broadcasts.append(0, broadcast, datetime, station)
            
            self.__gui.main_window.broadcasts_badge()
            
        self.__gui.dialog_planning.hide()
        

class Edit(BaseAction):    
    def __init__(self, gui):
        self.update_list = True
        self.__gui = gui

    def do(self, broadcast, planned_broadcasts):
        index = self.__gui.main_window.get_widget('treeview_planning').get_model().get_value(broadcast, 0)
        
        if self.__gui.dialog_planning.run_edit(planned_broadcasts[index]) == RESPONSE_OK:
            title, datetime, station = self.__gui.dialog_planning.get_values()
            planned_broadcasts[index].title = title
            planned_broadcasts[index].datetime = datetime
            planned_broadcasts[index].station = station
            
            self.__gui.main_window.broadcasts_badge()            
            
        self.__gui.dialog_planning.hide()

class Remove(BaseAction):    
    def __init__(self, gui):
        self.update_list = True
        self.__gui = gui

    def do(self, broadcasts, planned_broadcasts):
        if len(broadcasts) == 1:
            message = "Es ist eine Sendung ausgewählt. Soll diese Sendung "
        else:
            message = "Es sind %s Sendungen ausgewählt. Sollen diese Sendungen " % len(broadcasts)
        
        if self.__gui.question_box(message + "gelöscht werden?"):
            # convert indices to references in the list
            items = []
            for iter in broadcasts:
                index = self.__gui.main_window.get_widget('treeview_planning').get_model().get_value(iter, 0)
                items.append(planned_broadcasts[index])
            for item in items:
                planned_broadcasts.remove(item)
            
            self.__gui.main_window.broadcasts_badge()            
            
class Search(BaseAction):
    def __init__(self, gui):
        self.update_list = False
        self.__gui = gui
        
    def do(self, broadcasts, planned_broadcasts):
        for broadcast in broadcasts:
            index = self.__gui.main_window.get_widget('treeview_planning').get_model().get_value(broadcast, 0)
            broadcast = planned_broadcasts[index]
                        
            # build string: Titanic_08.12.24_20-15_pro7_
            string = broadcast.title.replace(' ', '_') + ' '
            string += time.strftime("%y.%m.%d_%H-%M", time.localtime(broadcast.datetime)) + "_"
            string += broadcast.station + "_"
            
            webbrowser.open("http://www.otr-search.com/?q=%s" % string)
            
class RSS(BaseAction):
    def __init__(self, gui):
        self.update_list = True
        self.__gui = gui
    
    def do(self, planned_broadcasts, email, rss_hash):
        url = "http://www.onlinetvrecorder.com/rss/my.php?email=%s&hash=%s" % (email, rss_hash)
    
        for broadcast in broadcasts:
            pass
