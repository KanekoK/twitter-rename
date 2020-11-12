## twitter-rename
Twitterのユーザー名をヤフー占いの双子座の恋愛運の結果で更新する

## セットアップ手順
Lambdaの環境変数にTwitter APIを使用するための
`CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_KEY`, `ACCESS_SECRET`を設定。

イベントトリガーのスケジュールを設定して、終了。

## Zappa導入

```bash
$ zappa init
```

### Lambdaへのデプロイ

### Lambdaへのデプロイ
```bash
$ zappa deploy prd
```

### Lambdaへの更新
```bash
$ zappa update prd
```
