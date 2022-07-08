from http.server import HTTPServer, CGIHTTPRequestHandler

class MyCGIHandler(CGIHTTPRequestHandler):
    # CGIプログラムを置くディレクトリ
    cgi_directories = ["/cgi-bin"]

# ポート番号の設定
LISTEN_PORT = 8080

if __name__ == "__main__":
	HOST, PORT = '', LISTEN_PORT

	# ポート番号を指定してアクセスすることに注意
	print("Access to http://localhost:8080/")

	# サーバ起動
	httpd = HTTPServer((HOST, PORT), MyCGIHandler)
	httpd.serve_forever()