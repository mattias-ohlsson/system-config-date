# Makefile for source rpm: system-config-date
# $Id$
NAME := system-config-date
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
