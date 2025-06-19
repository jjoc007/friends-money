output "api_url" {
  value = aws_apigatewayv2_stage.default.invoke_url
}

output "dynamodb_table" {
  value = aws_dynamodb_table.events.name
}

output "s3_bucket" {
  value = aws_s3_bucket.static.bucket
}
