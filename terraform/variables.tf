variable "project" {
  description = "Project name"
  type        = string
  default     = "friends-money"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet"
  type        = string
  default     = "10.0.0.0/24"
}

variable "private_subnet_cidr" {
  description = "CIDR block for the private subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "friendsdb"
}

variable "db_username" {
  description = "Database username"
  type        = string
  default     = "friends"
}

variable "db_password" {
  description = "Database password"
  type        = string
  default     = "changeme"
  sensitive   = true
}
