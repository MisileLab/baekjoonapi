import sentry_sdk
sentry_sdk.init(
    dsn="https://a81ff1e001514db192e946db52e4ee81@sentry.misilelaboratory.xyz/1",
    traces_sample_rate=1.0
)
