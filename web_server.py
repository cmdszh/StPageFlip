#!/usr/bin/env python3
import http.server
import socketserver
import sys
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        sys.stdout.write(f"{self.log_date_time_string()} - {format % args}\n")
        sys.stdout.flush()

    def end_headers(self):
        # 添加CORS头以便开发测试
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == "__main__":
    port = 8080
    
    # 设置当前工作目录
    os.chdir("/home/user/webapp")
    
    with socketserver.TCPServer(("0.0.0.0", port), MyHTTPRequestHandler) as httpd:
        print(f"服务器运行在端口 {port}")
        print(f"访问: http://localhost:{port}/example_hard_page_demo.html")
        sys.stdout.flush()
        httpd.serve_forever()