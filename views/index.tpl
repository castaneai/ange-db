<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width" />
        <title>アンジュ・ヴィエルジュ カードDB</title>
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
                -webkit-appearance: none;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 0.2em;
                font-size: larger;
                max-width: 100%;
                margin: 0.4em 0;
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
            .col-icon img {
                cursor: pointer;
            }
            
            /* 全身絵ビューアー */
            #viewer {
                position: fixed;
                display: none;
                width: 100%;
                height: 100%;
                background-position: center center;
                background-repeat: no-repeat;
                background-size: contain;
                background-color: rgba(0, 0, 0, 0.4);
            }
        </style>
    </head>
    <body>
        
        <div id="viewer">
        </div>

        <header>
            <h1>アンジュ・ヴィエルジュ カードDB</h1>
        </header>

        <div class="container">

            <form class="search-form" action="./" method="GET">
                <input type="text" name="keyword" placeholder="キャラ名，声優名など">
                <button type="submit">検索検索ぅ</button>
            </form>

            <table class="table">
                % for card in cards:
                <tr data-view-image="/images/character/{{ card.id }}.png">
                    <td class="col-icon"><a href="javascript:void(0);"><img src="/images/icon/{{ card.id }}.png" alt="{{ card.name }}" class="card-icon"></a></td>
                    <td class="col-name"><a href="javascript:void(0);"><strong>[{{ card.rarity }}]{{ card.name }}</strong></a></td>
                    <td class="col-parameters">
                        <ul>
                            <li>P: {{ card.power }}</li>
                            <li>G: {{ card.guard }}</li>
                            <li>S: {{ card.speed }}</li>
                        </ul>
                    </td>
                    <td class="col-profile">
                        <ul>
                            <li>IL: {{ card.illustrator }}</li>
                            <li>CV: {{ card.voice }}</li>
                        </ul>
                    </td>
                </tr>
                % end
            </table>
        </div>
        
        <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <script>
            $('.table tr a').on('click', function() {
                var viewImageUrl = $(this).parents('tr').attr('data-view-image');
                $('#viewer')
                .fadeIn('fast')
                .css('background-image', 'url(' + viewImageUrl + ')');
            });
            $('#viewer').on('click', function() {
                $(this).fadeOut('fast');
            });
        </script>
    </body>
</html>