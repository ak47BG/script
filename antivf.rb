#!/usr/bin/env ruby
# encoding: UTF-8
require 'net/http'
require 'open-uri'
require 'json'
require 'socket'
require 'optparse'

def banner()
red = "\033[01;31m"
green = "\033[01;32m"


puts "\n"
puts" █████╗ ███╗   ██╗████████╗██╗ ██████╗███████╗"
puts"██╔══██╗████╗  ██║╚══██╔══╝██║██╔════╝██╔════╝"
puts"███████║██╔██╗ ██║   ██║   ██║██║     █████╗"
puts"██╔══██║██║╚██╗██║   ██║   ██║██║     ██╔══╝"
puts"██║  ██║██║ ╚████║   ██║   ██║╚██████╗██║"
puts"╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝╚═╝"



puts "#{green}A simple tool written in Ruby for finding realtime ips behind CloudFlare."
puts "#{green}This tool is rather simple, it uses CrimeFlare to allow a bypass to CloudFlare protected domains."
puts "\n"
puts "#{green}Contact: #{red}https://twitter.com/PartialDuplex"
puts "\n"
puts "#{red}[!]This is a re-written version of the popular tool called 'HatCloud'. Many of the bugs have been fixed!"

puts "\n"
puts "#{green}Get Commands:"
puts "#{green}-h - Get the help for commands"
puts "\n"
end
