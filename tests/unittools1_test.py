#!/usr/bin/env python

import sys
import os
import unittest
import logging
import commands
#import config

#import unittools

log = logging

#outputdir = config.outputdir

class Case1(unittest.TestCase):
    
    def setUp(self):
        self.funcname = '_'.join(self.id().split('.')[-2:])
        log.info('setting up %s' % self.id())
        
    def tearDown(self):
		log.info('tearing down up %s' % self.id())
    
    def test1(self):
    	log.info(self.funcname)

    def test2(self):
    	log.info(self.funcname)

class Case2(unittest.TestCase):
    
    def setUp(self):
        self.funcname = '_'.join(self.id().split('.')[-2:])
        log.info('setting up %s' % self.id())
        
    def tearDown(self):
		log.info('tearing down up %s' % self.id())
    
    def test1(self):
    	log.info(self.funcname)
    
    def test2(self):
    	log.info(self.funcname)
    
    def test3(self):
    	log.info(self.funcname)

