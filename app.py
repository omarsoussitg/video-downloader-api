from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get_video', methods=['GET'])
def get_video():
    url = request.args.get('url')  # Get video URL from request
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        # Set yt-dlp options
        ydl_opts = {"quiet": True, "format": "best"}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)  # Fetch video details
            video_url = info.get("url", None)  # Get direct video link

        return jsonify({"video_url": video_url})  # Return the direct link

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
