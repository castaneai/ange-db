<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>アンジュDB</title>
        <style>
            * {
                margin: 0;
                padding: 0;
            }
            html, body {
                width: 100%;
                height: 100%;
            }
            body {
                font-family: 'Lucida Grande', 'Hiragino Kaku Gothic ProN', 'ヒラギノ角ゴ ProN W3', 'Meiryo', 'メイリオ', sans-serif;
                background: #ECF0F1;
                line-height: 1.6;
            }
            header {
                padding: 1em;
                text-align: center;
                background: #67809F;
                color: white;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                text-align: center;
            }
            .table {
                text-align: left;
                width: 100%;
            }
            .search-form {
                padding: 1em;
            }
            .search-form input,
            .search-form button {
                font-size: larger;
                max-width: 100%;
            }
            .table {
                border-collapse: collapse;
                word-break: break-all;
                table-layout: fixed;
            }
            .table td {
                font-size: smaller;
                padding: 0.2em;
            }
            .table li {
                list-style: none;
            }
            .table tr:nth-child(odd) {
                background: #d8e2e2;
            }
            .card-icon {
                max-width: 64px;
                height: auto;
            }
            .col-icon {
                text-align: center;
                width: 64px;
            }
            
            /* 全身絵ビューアー */
            #viewer {
                position: absolute;
                display: none;
                width: 100%;
                height: 100%;
            }
        </style>
    </head>
    <body>
        
        <div id="viewer">
        </div>

        <header>
            <h1>アンジュDB</h1>
        </header>

        <div class="container">

            <form class="search-form" action="/search" method="GET">
                <input type="text" name="keyword" placeholder="キャラ名，声優名などで検索">
                <button type="submit">検索検索ぅ</button>
            </form>

            <table class="table">
                % for card in cards:
                <tr>
                    <td class="col-icon"><a href="#" data-view-image="{{ card['image_url']['character'] }}"><img src="{{ card['image_url']['icon'] }}" alt="{{ card['name'] }}" class="card-icon"></a></td>
                    <td class="col-name"><strong>[{{ card['rarity'] }}]{{ card['name'] }}</strong></td>
                    <td class="col-parameters">
                        <ul>
                            <li>P: {{ card['parameters']['power'] }}</li>
                            <li>G: {{ card['parameters']['guard'] }}</li>
                            <li>S: {{ card['parameters']['speed'] }}</li>
                        </ul>
                    </td>
                    <td class="col-profile">CV: {{ card['creator']['voice'] }}</td>
                </tr>
                % end
            </table>
        </div>
        
        <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <script>
            $('.col-icon a').on('click', function() {
                var viewImageUrl = $(this).attr('data-view-image');
                $('#viewer').css({
                    'background-image': 'url(' + viewImageUrl + ')',
                    'background-position': 'center center',
                    'background-repeat': 'no-repeat',
                    'background-attachment': 'fixed',
                    'background-size': 'contain',
                    'background-color': 'rgba(0, 0, 0, 0.4)'
                }).fadeIn('fast');
            });
            $('#viewer').on('click', function() {
                $(this).fadeOut('fast');
            });
        </script>
    </body>
</html>