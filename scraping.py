import streamlit as st
import base64
import time

# ページ設定
st.set_page_config(page_title="スクレイピング UI", layout="wide")

# ロゴ画像を読み込み、Base64形式にエンコードする関数
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ロゴ画像のパスを指定
logo_path = "dodachallenge_logo.png"
logo_base64 = get_base64_of_bin_file(logo_path)

# ロゴマークエリアの追加
st.markdown(
    f"""
    <style>
    .logo-container {{
        background-color: #E0F7FA;
        padding: 10px;
        text-align: left;
        border-radius: 5px;
    }}
    .logo-container img {{
        width: 150px;  /* 画像の幅を150pxに制限 */
        height: auto;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" alt="dodaチャレンジロゴ">
    </div>
    """,
    unsafe_allow_html=True
)

# ページタイトル
st.title("dodaチャレンジ用スクレイピングツール")

# ログ用の初期化
if 'log_text' not in st.session_state:
    st.session_state.log_text = ""

# エラーハンドリング関数
def log_error(message):
    st.session_state.log_text += message + '\n'

# 上段のタブ
tab1, tab2, tab3 = st.tabs(["スクレイピング", "ロクイチリスト", "突合"])

with tab1:
    col6, col7 = st.columns([0.5, 3.5])
    with col6:
        st.markdown('<div class="left-align">', unsafe_allow_html=True)
        atcoder_checked = st.checkbox('AtCoder')
    with col7:
        st.markdown('<div class="left-align">', unsafe_allow_html=True)
        paiza_checked = st.checkbox('paiza')

    def scraping_process():
        try:
            # ステータスバーを表示
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.1)  # ダウンロードのシミュレーション
                progress_bar.progress(i)
            st.success("ダウンロード完了")
        except Exception as e:
            log_error(f'スクレイピングエラー: {str(e)}')
    
    if atcoder_checked or paiza_checked:
        if st.button('スクレイピングする', key='scraping_button'):
            scraping_process()

with tab2:
    st.markdown("### ロクイチリストをアップロード")
    col1, col2, col3, col4, col5, col6, col_gap3 = st.columns([1, 1, 1, 1, 1, 1, 5])
    with col1:
        if st.button('東京'):
            try:
                # 東京の処理をここに追加
                st.write('東京のアップロード完了')
            except Exception as e:
                log_error(f'東京エラー: {str(e)}')
    with col2:
        if st.button('千葉'):
            try:
                # 千葉の処理をここに追加
                st.write('東京のアップロード完了')
            except Exception as e:
                log_error(f'千葉エラー: {str(e)}')
    with col3:
        if st.button('埼玉'):
            try:
                # 埼玉の処理をここに追加
                st.write('埼玉のアップロード完了')
            except Exception as e:
                log_error(f'埼玉エラー: {str(e)}')
    with col4:
        if st.button('京都'):
            try:
                # 京都の処理をここに追加
                st.write('京都のアップロード完了')
            except Exception as e:
                log_error(f'京都エラー: {str(e)}')
    with col5:
        if st.button('大阪'):
            try:
                # 大阪の処理をここに追加
                st.write('大阪のアップロード完了')
            except Exception as e:
                log_error(f'大阪エラー: {str(e)}')
    with col6:
        if st.button('福岡'):
            try:
                # 福岡の処理をここに追加
                st.write('福岡のアップロード完了')
            except Exception as e:
                log_error(f'福岡エラー: {str(e)}')

with tab3:
    col9, = st.columns([2])
    with col9:
        if st.button('突合する'):
            try:
                # 突合処理をここに追加
                st.write('突合が開始されました')
            except Exception as e:
                log_error(f'突合エラー: {str(e)}')

# ログ出力用テキストエリア
st.markdown("### ログ")
st.text_area("ログ出力", st.session_state.log_text, height=100)
